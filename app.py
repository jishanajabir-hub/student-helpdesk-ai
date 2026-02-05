import streamlit as st

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🎓 Student Helpdesk Bot")
st.write("Welcome! Ask me about fees, courses, or hostel.")

if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.user_input = ""
    st.rerun()

question = st.text_input("Ask your question:", key="user_input")
faq = {
    "fee": "💰 Fee Structure: The average annual fee ranges from ₹50,000 to ₹1,20,000 depending on the course.",
    "hostel": "🏠 Hostel Facility: Separate hostels for boys and girls with food and Wi-Fi.",
    "course": "📚 Courses Offered: Engineering, Arts, Science, Commerce, and Management."
}

if question:
    responses = []

    for key, answer in faq.items():
        if key in question.lower():
            responses.append(answer)

    if not responses:
        responses.append("❓ Sorry, I don't understand that yet.")

    st.session_state.chat_history.append(("You", question))
    for res in responses:
        st.session_state.chat_history.append(("Bot", res))


st.markdown("---")
for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")
