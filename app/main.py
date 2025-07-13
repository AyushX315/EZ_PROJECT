from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
# from app.document_parser import extract_text
# from app.summarizer import summarize_text
# from app.qa_engine import answer_question
# from app.question_generator import generate_questions
# from app.evaluator import evaluate_answer

from app.document_parser import extract_text
from app.summarizer import summarize_text
from app.qa_engine import answer_question
from app.question_generator import generate_questions
from app.evaluator import evaluate_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

doc_text = ""

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    global doc_text
    ext = file.filename.split('.')[-1]
    doc_text = extract_text(await file.read(), ext)
    return {"summary": summarize_text(doc_text)}

@app.get("/ask/")
def ask(q: str):
    global doc_text
    return answer_question(doc_text, q)

@app.get("/challenge/")
def challenge():
    global doc_text
    return generate_questions(doc_text)

@app.post("/evaluate/")
def evaluate(user_answer: str = Form(...), expected: str = Form(...)):
    return evaluate_answer(user_answer, expected)
