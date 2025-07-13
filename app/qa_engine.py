from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_question(context, question):
    result = qa_pipeline(question=question, context=context)
    answer = result['answer']
    score = result['score']
    return {
        "answer": answer,
        "confidence": f"{score:.2f}",
        "justification": f"This is based on the extracted content with score: {score:.2f}"
    }
