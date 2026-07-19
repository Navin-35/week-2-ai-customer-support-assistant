# 🤖 AI Customer Support Assistant

An AI-powered customer support chatbot built using **Flask**, **LangChain**, and **Google Gemini**. It answers customer queries using prompt engineering, a predefined knowledge base, and structured AI responses.

## 🚀 Features

- AI-powered customer support chatbot
- Google Gemini integration
- LangChain Prompt Templates
- Knowledge-based responses
- Structured JSON output
- Flask REST API
- Interactive web interface

## 🛠️ Tech Stack

- Python
- Flask
- LangChain
- Google Gemini API
- HTML, CSS, JavaScript
- Pydantic

## 📂 Project Structure

```text
├── app.py
├── chatbot.py
├── prompts.py
├── parser.py
├── knowledge_base.py
├── templates/
├── static/
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/Navin-35/week-2-ai-customer-support-assistant.git

cd week-2-ai-customer-support-assistant

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the project:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## 💬 Sample Questions

- Where is my order?
- How long does shipping take?
- Can I return a product?
- What payment methods are accepted?
- Do you provide warranty?

## 📸 Screenshots

Add screenshots of the application in the `screenshots` folder.

## 👨‍💻 Author

**Navin Kumar**

GitHub: https://github.com/Navin-35

## 📄 License

This project was developed as part of the **DStarix Generative AI Internship – Week 2** for learning and portfolio purposes.