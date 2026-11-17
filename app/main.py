from fastapi import FastAPI

app = FastAPI(title="secure-bff-azure")

@app.get("/health")
def health():
    return {"status": "ok"}