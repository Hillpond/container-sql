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
    try:
        cursor.execute(f"USE {userSchemaName}")  # Select database ur working in
        results = []
        columns = []
        affected_rows = 0
        for command in queryString.split(";"):
          command = command.strip()

          if not command:
            continue

          cursor.execute(command)
        if cursor.with_rows:
            results = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
        else:
            if cursor.rowcount != -1:
                affected_rows += cursor.rowcount
        mydb.commit()
        print("Query sent successfully")
        return {
            "columns": columns,
            "rows" : results,
            "affected_rows" : affected_rows
        }
    except Exception as e:
        mydb.rollback()
        raise Exception(f"Query failed: {e}")
    finally:
        cursor.close()
        mydb.close()




