from llama_index import GPTVectorStoreIndex
from pathlib import Path
from llama_index import download_loader
PDFReader = download_loader ("PDFReader")
loader = PDFReader()
documents = loader.load_data(file=Path("site-reliability-engineering-handbook.pdf"))
index = GPTVectorStoreIndex.from_documents(documents)
index.storage_context.persist("site-reliability-engineer-handbook")