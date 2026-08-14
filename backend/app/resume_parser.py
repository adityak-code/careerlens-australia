import fitz

def extract_text_from_pdf(file_bytes: bytes)-> str:
    """
    Extract text from PDF file using PyMuPDF.
    file_bytes means PDF content in bytes."""

    text=""
    #open pdf in bytes
    pdf_document = fitz.open(stream = file_bytes, filetype="pdf")

    #Loop through pages
    for page in pdf_document:
        page_text = page.get_text()
        text += page_text + "\n"

    pdf_document.close()
    return text.strip()