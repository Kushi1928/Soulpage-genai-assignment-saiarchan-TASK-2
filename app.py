import streamlit as st
from bot import chat_with_bot

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Knowledge Bot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* App background */
.stApp {
    background: linear-gradient(135deg, #000000, #1c1c1c, #2b2b2b);
    color: #ffffff;
}

/* Title */
h1 {
    text-align: center;
    font-weight: 600;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    opacity: 0.75;
    margin-bottom: 20px;
}

/* Chat container */
.chat-container {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
    margin-bottom: 10px;
}

/* User message */
.user-msg {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 12px 16px;
    border-radius: 18px;
    margin: 8px 0;
    text-align: right;
}

/* Bot message */
.bot-msg {
    background: rgba(255, 255, 255, 0.15);
    padding: 12px 16px;
    border-radius: 18px;
    margin: 8px 0;
    text-align: left;
}

/* Chat input */
.stChatInput textarea {
    background: #000000 !important;
    color: #ffffff !important;
    border-radius: 14px;
    border: 1px solid #333333;
}

/* Placeholder */
.stChatInput textarea::placeholder {
    color: #aaaaaa;
}

/* Focus */
.stChatInput textarea:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 1px #667eea;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("""
<h1>🤖 Conversational Knowledge Bot</h1>
<p class="subtitle">
Powered by Gemini API • Context Memory • Web Search
</p>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- CHAT UI ----------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div class='user-msg'>🧑‍💻 {msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='bot-msg'>🤖 {msg['content']}</div>",
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    history_text = ""
    for m in st.session_state.messages:
        role = "User" if m["role"] == "user" else "Assistant"
        history_text += f"{role}: {m['content']}\n"

    with st.spinner("Thinking..."):
        response = chat_with_bot(user_input, history_text)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()
