import os
from fastapi import UploadFile


def upload_files(file: UploadFile):
    save_path = os.path.join("Functions", "Admin", "DB's", file.filename)

    with open(save_path, "wb") as file:
        contents =  file.read()
        file.write(contents)

    return {"message": f"{file.filename} lastet opp"}







