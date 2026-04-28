
from fastapi import FastAPI, UploadFile, File
from starlette.responses import FileResponse
from Functions.Admin.deleteFile import deleteFile
from Functions.Admin.setSelectedFile import setSelectedFile
from Functions.Admin.getSelectedFile import getSelectedFile
from Functions.Admin.showAllFiles import showAllFiles
from Functions.Admin.upload_File import upload_files
from Functions.User.querySend import querySend
from fastapi.middleware.cors import CORSMiddleware
from Functions.createSchemaBasedOnSession  import createSchemaBasedOnSession
from Functions.makeTablesOnStartup import makeTablesOnStartup
from Functions.recreateTables import recreateTables

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/query")
def run_query(sql: str, userSchemaName: str):
    results = querySend(sql, userSchemaName)
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

@app.delete("/admin/delete/{filename}")
async def delete_file(filename: str):
    result = await deleteFile("Functions/Admin/DB's/" + filename)
    return result

#henter localSession for å lage schema
@app.post("/session/init")
async def init_session(userSchemaName: str):
    # 1) Lag schemaet først (idempotent: gjør ingenting hvis det finnes)
    createSchemaBasedOnSession(userSchemaName)
    # 2) Deretter bygg tabellene fra admin-fila inn i schemaet
    return await makeTablesOnStartup(userSchemaName)


@app.post("/session/recreate")
async def recreate_tables(userSchemaName: str):
    await recreateTables(userSchemaName)
    return {"ok": True, "message": f"Tabeller gjenskapt i {userSchemaName}"}

#test
@app.get("/admin")
async def admin_page():
    return FileResponse("Web-Page/admin.html")

@app.get("/")
async def user_page():
    return FileResponse("Web-Page/page.html")
