
from fastapi import FastAPI, UploadFile, File
from starlette.responses import FileResponse

from Functions.Admin.setSelectedFile import setSelectedFile
from Functions.Admin.getSelectedFile import getSelectedFile
from Functions.Admin.showAllFiles import showAllFiles
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
    return results

@app.post("/admin/upload")
async def upload_endpoint(file: UploadFile = File(...)):
    return await upload_files(file)

@app.get("/admin/files")
async def list_files():
    files = await showAllFiles()
    return {"files": files}

@app.post("/admin/select/{filename}")
async def select_file(filename: str):
    await setSelectedFile(filename)
    return {"selected": filename}

@app.get("/admin/selected")
async def get_selected():
    selected = await getSelectedFile()
    return {"selected": selected}

#test
@app.get("/admin")
async def admin_page():
    return FileResponse("Web-Page/admin.html")

@app.get("/")
async def user_page():
    return FileResponse("Web-Page/page.html")
