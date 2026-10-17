# Study Buddy — Demo

Study Buddy is a small local Streamlit study-chat interface built for a short hackathon proof of concept. This repository contains the demo-mode code and safe project documentation.

Quick start (Windows):

1. python -m venv .venv
2. .venv\Scripts\activate
3. pip install -r requirements.txt
4. python -m streamlit run app.py

The app defaults to a no-cost demo mode. It locally counts frequent words from pasted text and clearly labels them as a simple hint—not an AI-generated summary. No API request is sent unless live AI is deliberately enabled. See `devpost/` for the project plans and app map.

Do not commit `.env` or any private keys. A safe example is provided in `.env.example`.
