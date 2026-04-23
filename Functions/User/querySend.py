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

def querySend(queryString):
    for command in queryString.split(";"):
      command = command.strip()

      if not command:
        continue

      cursor.execute(command)
    results = cursor.fetchall()
    print(results)
    mydb.commit()
    print("Query sent successfully")
    return {
        "columns": [col[0] for col in cursor.description], 
        "rows" : results
    }




testquery = "SELECT * FROM lege;"

querySend(testquery)



