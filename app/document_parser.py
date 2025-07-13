import fitz

def extract_text(file_bytes, extension):
    if extension.lower() == 'pdf':
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        return "\n".join(page.get_text() for page in doc)
    elif extension.lower() == 'txt':
        return file_bytes.decode('utf-8')
    else:
        raise ValueError("Unsupported file type")
