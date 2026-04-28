import mysql.connector

#oppretter kobling til databasen
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


#Variables
pathToSchemaScript = "DB's/"


def querySend(queryString,userSchemaName):
    mydb = connectToMySQL()
    # lager et cursor objekt, funker litt som hvor / hva man gjør i databasen
    cursor = mydb.cursor()
    cursor.execute(f"USE {userSchemaName}")  # Select database ur working in
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




