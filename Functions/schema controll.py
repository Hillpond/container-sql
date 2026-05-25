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



#henter alle schema navn i databasen
def getAllSchemaNames():
    scemalist = []
    mydb = connectToMySQL()
    cursor = mydb.cursor()
    cursor.execute("SHOW SCHEMAS")
    schemas = cursor.fetchall()

    # schema som ikke skal med
    DontWant = ['mysql', 'sys', 'information_schema', 'performance_schema']

    for schema in schemas:
        schemaNameAsString = schema[0]  # tar bare med string ikke tuppel :clown:
        if schemaNameAsString not in DontWant:
            scemalist.append(schemaNameAsString)

    return scemalist



def killSchemas(activeSchemaList):
    currentSchemasInDB = getAllSchemaNames()
    schemasToKill = []

    for schema in currentSchemasInDB:
        if schema not in activeSchemaList:
            schemasToKill.append(schema)

    mydb = connectToMySQL()
    cursor = mydb.cursor()
    for schema in schemasToKill:
        cursor.execute(f"Drop SCHEMA {schema}")








