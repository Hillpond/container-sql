from fastapi import FastAPI

from Functions.User.querySend import querySend

app = FastAPI()

@app.get("/query")
def run_query(sql: str):
    results = querySend(sql)
    return {"results": results}