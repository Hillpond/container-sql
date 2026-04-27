import mysql.connector
import asyncio

from Functions.Admin.getSelectedFile import getSelectedFile

#oppretter kobling til databasen
mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="root",
  passwd="pass"
)

# lager et cursor objekt, funker litt som hvor / hva man gjør i databasen
cursor = mydb.cursor()

#Variables



#making tables form sql file:
async def makeTablesOnStartup(userSchemaName):
  selectedFile = await getSelectedFile()
  pathToSchemaScript = "Functions/Admin/DB's/" + selectedFile
  cursor.execute(f"USE {userSchemaName}")  # Select database ur working in (need to get the info from local session)
  with open(pathToSchemaScript, "r", encoding="utf-8") as f:
    sqlScript = f.read()
  for command in sqlScript.split(";"):
    command = command.strip() #fjerner mellomromm og enter(tommre rom)
    if not command:
      continue
    print (command)
    cursor.execute(command)
  mydb.commit()




















