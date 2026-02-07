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
<<<<<<< HEAD
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
=======
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
>>>>>>> 9d07cdb80ff8ce1f358cbfbe542557e8e1b79e0b
│
├── requirements.txt
│   └── Project dependencies
│       - streamlit
<<<<<<< HEAD
│       - python libraries
=======
│       - transformers
│       - torch
>>>>>>> 9d07cdb80ff8ce1f358cbfbe542557e8e1b79e0b
│
├── README.md
│   └── Project documentation
│       - Overview
│       - Features
│       - Setup instructions
│       - Project structure
│
└── .gitignore
<<<<<<< HEAD
    └── Files ignored by Git
=======
    └── Files and folders ignored by Git

>>>>>>> 9d07cdb80ff8ce1f358cbfbe542557e8e1b79e0b
