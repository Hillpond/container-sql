import mysql.connector

#oppretter kobling til databasen
mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="root",
  passwd="pass",
)


# lager et cursor objekt, funker litt som hvor / hva man gjør i databasen
cursor = mydb.cursor()

#Variables
pathToSchemaScript = "DB's/"


#Select database ur working in
databaseName = "mydb"
cursor.execute("USE " + databaseName + " ;")



