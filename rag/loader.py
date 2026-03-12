from pathlib import Path
from config.settings import settings

def load_documents():

    docs = []

    for file in Path(settings.DATA_PATH).glob("*.txt"):

        with open(file, "r", encoding="utf-8") as f:
            docs.append(f.read())

    return docs
