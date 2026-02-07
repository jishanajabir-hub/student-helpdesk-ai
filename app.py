import streamlit as st
from data import get_response
from fallback import fallback_response

st.set_page_config(page_title="Student Helpdesk Chatbot", page_icon="🎓")

st.title("🎓 Student Helpdesk Chatbot")
st.caption("Ask about admissions, fees, courses, exams, or general study topics")

# Session state for chat
if "chat" not in st.session_state:
    st.session_state.chat = []

# Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.chat = []
    st.rerun()

# User input
user_query = st.text_input("Ask your question")

if user_query:
    reply = get_response(user_query)

    if reply == "NOT_FOUND":
        reply = fallback_response(user_query)

    st.session_state.chat.append(("You", user_query))
    st.session_state.chat.append(("Bot", reply))

# Display chat
st.markdown("---")
for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(f"🧑 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")
