from openai import OpenAI

client = OpenAI(api_key="PASTE_YOUR_API_KEY_HERE")

def ai_response(user_query):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful student assistant."},
            {"role": "user", "content": user_query}
        ]
    )

    return response.choices[0].message.content
