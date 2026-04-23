import os

SELECTED_FILE = os.path.join(os.path.dirname(__file__), "selected.txt")

async def getSelectedFile() -> str:
    if not os.path.exists(SELECTED_FILE):
        return None
    with open(SELECTED_FILE, "r") as f:
        return f.read().strip()