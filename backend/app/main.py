from fastapi import FastAPI

app = FastAPI(title="CareerLens Australia API")

@app.get("/health")
def health_check():
    return {"status": "CareerLens backend is running"}