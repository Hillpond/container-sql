
from fastapi import FastAPI, UploadFile, File

from Functions.Admin.upload_File import upload_files
from Functions.User.querySend import querySend

app = FastAPI()

@app.get("/query")
def run_query(sql: str):
    results = querySend(sql)
    return {"results": results}

@app.post("/admin/upload")
async def upload_endpoint(file: UploadFile = File(...)):
    return await upload_files(file)


