import mysql.connector

#oppretter kobling til databasen
mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="root",
  passwd="pass",
)

curser = mydb.cursor()

curser.execute('CREATE Schema mydb')

