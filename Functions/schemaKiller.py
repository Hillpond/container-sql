import time
import threading
import mysql.connector

# schema_name
ACTIVE_SCHEMAS = {}

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

def deleteSchema():
        activeSchemaList = list(ACTIVE_SCHEMAS.keys())  # list from
        killSchemas(activeSchemaList)

def cleanupSchemas():
    while True:
        now = time.time()
        expired = []
        for schema_name, last_seen in ACTIVE_SCHEMAS.items():
            # older than 10 minutes
            if now - last_seen > 6:
                expired.append(schema_name)
        for schema_name in expired:
            del ACTIVE_SCHEMAS[schema_name]
        print("ACTIVE_SCHEMAS:", ACTIVE_SCHEMAS)
        time.sleep(5)
        deleteSchema()
threading.Thread(
    target=cleanupSchemas,
    daemon=True
).start()



