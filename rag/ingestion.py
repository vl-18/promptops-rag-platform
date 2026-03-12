from pathlib import Path
from config.settings import settings


class DocumentIngestor:

    def load_documents(self):

        documents = []

        data_path = Path(settings.DATA_PATH)

        for file in data_path.glob("*.txt"):

            with open(file, "r", encoding="utf-8") as f:

                documents.append({
                    "content": f.read(),
                    "source": file.name
                })

        return documents


    def chunk_text(self, text):

        chunk_size = settings.CHUNK_SIZE
        overlap = settings.CHUNK_OVERLAP

        chunks = []
        start = 0

        while start < len(text):

            end = start + chunk_size
            chunks.append(text[start:end])

            start += chunk_size - overlap

        return chunks


    def create_chunks(self, documents):

        all_chunks = []

        for doc in documents:

            chunks = self.chunk_text(doc["content"])

            for chunk in chunks:

                all_chunks.append({
                    "content": chunk,
                    "source": doc["source"]
                })

        return all_chunks