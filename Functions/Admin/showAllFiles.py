import os

fileLocation = "Functions/Admin/DB's"


async def showAllFiles():
    if not os.path.exists(fileLocation):
        return []

    files = []
    for filename in os.listdir(fileLocation):
        files.append({
            "name": filename
        })
    return files