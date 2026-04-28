import mysql.connector
import asyncio

from Functions.Admin.getSelectedFile import getSelectedFile

def connectToMySQL():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            passwd="pass"
        )
        return mydb
    except Exception as e:
        return "Error connecting to MySQL"

async def recreateTables(userSchemaName):
    mydb = connectToMySQL()
    cursor = mydb.cursor()
    cursor.execute(f"USE {userSchemaName}")

    # Hent alle tabeller først
    cursor.execute("SHOW TABLES")
    tables = [t[0] for t in cursor.fetchall()]  

    # Slett alle tabeller
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS `{table}`")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    mydb.commit()

    # Bygg tabellene på nytt fra SQL-filen
    selectedFile = await getSelectedFile()
    pathToSchemaScript = "Functions/Admin/DB's/" + selectedFile
    cursor.execute(f"USE {userSchemaName}")
    with open(pathToSchemaScript, "r", encoding="utf-8") as f:
        sqlScript = f.read()
    for command in sqlScript.split(";"):
        command = command.strip()
        if not command:
            continue
        print(command)
        cursor.execute(command)
    mydb.commit()