import pypdf
import docx2txt
import tempfile
from typing import Any

# Extracts raw text from PDF or DOCX resumes
def extract_text(uploaded_file: Any) -> str:
    if uploaded_file.name.lower().endswith('.pdf'):
        reader = pypdf.PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or '' for page in reader.pages)
    elif uploaded_file.name.lower().endswith('.docx'):
        # docx2txt expects a file path
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp.write(uploaded_file.read())
            tmp.flush()
            text = docx2txt.process(tmp.name)
        return text
    else:
        return ""
