from transformers import pipeline

# Load lightweight instruction-following model
generator = pipeline(
    "text-generation",
    model="google/flan-t5-small",
    max_new_tokens=120
)

def ai_response(user_query):
    prompt = f"""
You are a helpful student helpdesk assistant.
Answer the question clearly and in simple language.

Question: {user_query}
Answer:
"""
    result = generator(prompt)
    return result[0]["generated_text"]
