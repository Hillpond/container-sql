import mysql.connector

# oppretter kobling til databasen
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


def createSchemaBasedOnSession(userSchemaName):
    mydb = connectToMySQL()
    cursor = mydb.cursor()
    cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {userSchemaName}")
    mydb.commit()









