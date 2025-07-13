from transformers import pipeline

evaluation = pipeline("text-generation", model="gpt2")

def evaluate_answer(user_answer, correct_answer):
    prompt = f"Compare the following:\nUser Answer: {user_answer}\nCorrect Answer: {correct_answer}\nGive a score out of 10 and a brief justification."
    response = evaluation(prompt, max_length=100, num_return_sequences=1)
    return {"feedback": response[0]["generated_text"]}
