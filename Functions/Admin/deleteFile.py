import os

async def deleteFile(filePath):
    if not os.path.exists(filePath):
        return {"ok": False, "message": "Filen finnes ikke"}
    os.remove(filePath)
    return {"ok": True, "message": f"{filePath} slettet"}