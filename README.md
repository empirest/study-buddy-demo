# Study Buddy — Demo

Study Buddy is a small local Streamlit study-chat interface built for a short hackathon proof of concept. This repository contains the demo-mode code and safe project documentation.

Quick start (Windows):

1. python -m venv .venv
2. .venv\Scripts\activate
3. pip install -r requirements.txt
4. python -m streamlit run app.py

The app defaults to a no-cost demo mode that explicitly shows a notice instead of sending pasted text to an AI provider. See `devpost/` for the scope, PRD, spec, checklist, and a compact app map (`devpost/app-map.html`) that explains where the demo notice appears in the code.

Do not commit `.env` or any private keys. A safe example is provided in `.env.example`.
