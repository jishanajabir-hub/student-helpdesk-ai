from ai_fallback import ai_response

def fallback_response(user_query):
    try:
        return ai_response(user_query)
    except Exception:
        return "🤖 I'm still learning. Please try again in a moment."
