# 🎓 Student Helpdesk AI Chatbot
🎯 A beginner-friendly AI chatbot project built to simulate a real college student helpdesk.

This project is a Student Helpdesk Chatbot built using Python and Streamlit.

A domain-specific chatbot built using **Python** and **Streamlit** to assist students with common academic and administrative queries.  
This project demonstrates chatbot logic, basic NLP-style intent handling, session-based chat memory, and a clean user interface.

---

## 📌 Project Overview

The **Student Helpdesk AI Chatbot** is designed to answer frequently asked questions related to:
- Admissions
- Courses
- Fees
- Exams
- General study-related topics

The chatbot uses a **rule-based approach** for domain-specific queries and a **smart fallback mechanism** for general questions, making it reliable, fast, and beginner-friendly.

---

## ✨ Key Features

- 🎓 Handles admission-related queries  
- 💰 Provides fee information  
- 📚 Answers course and exam questions  
- 🤖 Smart fallback responses for general knowledge  
- 🧠 Chat history using Streamlit session state  
- 🧹 Clear chat functionality  
- 🖥️ Simple and clean user interface  

---

## 🛠️ Tech Stack

Language: Python

Frontend: Streamlit

AI Model: HuggingFace Transformers

Version Control: Git & GitHub

Deployment: Streamlit Cloud

---

## 📂 Project Structure

'''bash

student-helpdesk-ai/
│
├── app.py
│   └── Main Streamlit application
│       - Handles UI and user interaction
│       - Manages chat history using session state
│       - Connects rule-based logic with AI fallback
│
├── data.py
│   └── Rule-based response engine
│       - Handles predefined student queries
│       - Topics: admissions, fees, exams, courses, hostel
│
├── fallback.py
│   └── Smart fallback handler
│       - Triggers AI response when no rule-based match is found
│       - Ensures smooth user experience for unknown questions
│
├── ai_fallback.py
│   └── HuggingFace AI integration
│       - Uses a lightweight transformer model
│       - Generates AI-powered answers for general questions
│
├── requirements.txt
│   └── Project dependencies
│       - streamlit
│       - transformers
│       - torch
│
├── README.md
│   └── Project documentation
│       - Overview
│       - Features
│       - Setup instructions
│       - Project structure
│
└── .gitignore
    └── Files and folders ignored by Git
    
'''
---

## 🚀 Future Improvements
- Add HuggingFace AI fallback
- Improve NLP intent detection
- Add user authentication
- Deploy on Streamlit Cloud

---

## 👩‍💻 Author
**Jishana Jabir**  
Beginner AI & Data Science Enthusiast

⭐ If you like this project, give it a star!
