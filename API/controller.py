from fastapi import FastAPI

app = FastAPI()

@app.get("/query")
def run_query(sql: str):
    results = querySend(sql)
    return {"results": results}