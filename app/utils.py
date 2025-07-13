def chunk_text(text, size=512):
    return [text[i:i+size] for i in range(0, len(text), size)]
