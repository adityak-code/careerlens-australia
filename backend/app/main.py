from fastapi import FastAPI, UploadFile, File
from app.resume_parser import extract_text_from_pdf

app = FastAPI(title="CareerLens Australia API")

@app.get("/health")
def health_check():
    return {"status": "CareerLens backend is running"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    file_bytes = await file.read()
    extracted_text = extract_text_from_pdf(file_bytes)

    return {"filename": file.filename,
            "content_type": file.content_type,
            "text_preview": extracted_text[:1000],  # Return first 1000 characters of extracted text
            "total_characters": len(extracted_text),
            "message": "Resume uploaded successfully"}
    
