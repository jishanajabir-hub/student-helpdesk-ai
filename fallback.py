def fallback_response(query):
    q = query.lower()

    if "artificial intelligence" in q or "ai" in q:
        return "🤖 Artificial Intelligence is the simulation of human intelligence in machines that can think, learn, and make decisions."

    elif "data science" in q:
        return "📊 Data Science is the field of analyzing data to extract insights using statistics, programming, and machine learning."

    elif "prepare" in q and "exam" in q:
        return "📚 To prepare for exams: make a study plan, revise daily, practice questions, and take short breaks."

    else:
        return "❓ I'm still learning. Please ask about admissions, fees, courses, or exams."
