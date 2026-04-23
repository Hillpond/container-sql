import os

SELECTED_FILE = os.path.join(os.path.dirname(__file__), "selected.txt")

async def setSelectedFile(filename: str):
    with open(SELECTED_FILE, "w") as f:
        f.write(filename)
