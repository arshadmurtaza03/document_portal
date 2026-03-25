import importlib.metadata
packages = [
    "langchain",
    "python-dotenv",
    "ipykernel",
    "langchain_groq",
    "langchain_google_genai",
    "langchain-community",
    "langchain-core",
    "langchain-text-splitters",
    "langchain-huggingface",
    "sentence-transformers",
    "pandas",
    "faiss-cpu",
    "structlog",
    "pypdf",
    "PyMuPDF",
    "pylint",
    "langchain-core",
    "pytest",
    "streamlit",
    "fastapi",
    "uvicorn",
    "python-multipart",
    "docx2txt"
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")

# # serve static & templates
# app.mount("/static", StaticFiles(directory="../static"), name="static")
# templates = Jinja2Templates(directory="../templates")