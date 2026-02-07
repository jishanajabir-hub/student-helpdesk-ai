def get_response(user_query):
    user_query = user_query.lower()

    if "admission" in user_query:
        return "🎓 Admission Process:\n• Fill the online form\n• Submit documents\n• Attend interview\n• Pay fees"

    elif "courses" in user_query:
        return "📘 Available Courses:\n• B.Com\n• B.Sc\n• BCA\n• MBA"

    elif "fees" in user_query:
        return "💰 Fee Structure:\n₹50,000 – ₹1,20,000 per year"

    else:
        return "NOT_FOUND"
