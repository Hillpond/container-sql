
from fastapi import FastAPI, UploadFile, File

from Functions.Admin.upload_File import upload_files
from Functions.User.querySend import querySend
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/query")
def run_query(sql: str):
    results = querySend(sql)
    return {"results": results}

@app.post("/admin/upload")
async def upload_endpoint(file: UploadFile = File(...)):
    return await upload_files(file)


