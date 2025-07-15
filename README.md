# Font-filtering-security

#🛡️ Font Filtering Secure Chatbot (Streamlit + Ollama)
This project is an intelligent, privacy-focused chatbot interface built with Streamlit and powered by Ollama LLM (LLaMA 3.2). It features a custom React-based input box that filters out sensitive text based on specific font properties (like "Courier New"). The app remembers the last few turns in a conversation using LangChain's memory capabilities and offers a modern, pinned-chat UI similar to ChatGPT.

#✨ Features
🔐 Font Security Filtering
Custom text box removes text with restricted fonts (e.g., Courier New) before sending to the LLM.

🤖 LLM-Powered Conversations
Uses Ollama's llama3.2:latest model for contextual and memory-based responses.

📌 Pinned Chat Input
Custom Streamlit component keeps the chat box fixed at the bottom center like modern chat apps.

🧠 Chat Memory
Recalls the last 5 turns of conversation to give context-aware replies.

🧼 Clear & Stop Buttons
Easily reset the chat when needed.

🎨 Minimal UI with Auto-Scroll and Sidebar Tools

🛠️ Tech Stack
Python, Streamlit

LangChain (for LLM chaining and memory)

Ollama (LLaMA 3.2 model)

React + TypeScript (for custom component)

#🔧 Setup Instructions
Clone the repo
git clone https://github.com/your-username/Font-filtering-security.git

Install requirements
pip install -r requirements.txt

Run the app
streamlit run main.py
