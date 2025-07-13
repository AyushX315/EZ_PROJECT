from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_questions(text):
    prompt = f"Generate 3 logic-based or comprehension questions based on this document:\n\n{text[:1000]}"
    questions = generator(prompt, max_length=256, num_return_sequences=1)
    return {"questions": questions[0]['generated_text'].split('\n')[1:4]}
