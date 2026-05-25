import time
import threading

# schema_name
ACTIVE_SCHEMAS = {}


def cleanupSchemas():
    while True:
        now = time.time()
        expired = []
        for schema_name, last_seen in ACTIVE_SCHEMAS.items():
            # older than 10 minutes
            if now - last_seen > 600:
                expired.append(schema_name)
        for schema_name in expired:
            del ACTIVE_SCHEMAS[schema_name]
        print("ACTIVE_SCHEMAS:", ACTIVE_SCHEMAS)
        time.sleep(30)
threading.Thread(
    target=cleanupSchemas,
    daemon=True
).start()