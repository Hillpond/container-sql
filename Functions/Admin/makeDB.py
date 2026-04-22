import mysql.connector

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
scriptFolder = "DB's/"


#Select database ur working in
databaseName = "mydb"

cursor.execute("USE " + databaseName + " ;")

#making tables form sql file:
def makeTables(pathToSchemaScript):
  with open(pathToSchemaScript, "r", encoding="utf-8") as f:
    sqlScript = f.read()
  for command in sqlScript.split(";"):
    command = command.strip() #fjerner mellomromm og enter(tommre rom)
    if not command:
      continue
    print (command)
    cursor.execute(command)
  mydb.commit()

makeTables(scriptFolder + "LegeTable.sql")


cursor.execute("SHOW TABLES")
print("\ntabller opprettet:")
for table in cursor:
  print (table)



















