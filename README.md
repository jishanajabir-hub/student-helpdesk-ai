# 🎓 Student Helpdesk AI Chatbot

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

- **Python**
- **Streamlit**
- Rule-based NLP logic
- Session state management

---

## 📂 Project Structure
student-helpdesk-ai/
│
├── app.py
│   └── Main Streamlit application
│       - Handles UI
│       - Manages chat history
│       - Connects rule-based + AI fallback responses
│
├── data.py
│   └── Rule-based responses (FAQs)
│       - Admissions
│       - Courses
│       - Fees
│       - Hostel
│       - Exams, etc.
│
├── fallback.py
│   └── Smart fallback responses
│       - Handles unknown questions
│       - Provides generic helpful answers
│
├── requirements.txt
│   └── Project dependencies
│       - streamlit
│       - python libraries
│
├── README.md
│   └── Project documentation
│       - Overview
│       - Features
│       - Setup instructions
│       - Project structure
│
└── .gitignore
    └── Files ignored by Git
