import streamlit as st
from langchain_groq import ChatGroq

# Page config (Premium Look)
st.set_page_config(
    page_title="HS AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for premium UI
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.chat-container {
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 10px;
}
.user-msg {
    background-color: #2563eb;
    color: white;
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
}
.bot-msg {
    background-color: #1e293b;
    color: #e2e8f0;
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
}
.title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🤖 HS AI Chatbot</div>', unsafe_allow_html=True)

# Initialize session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key="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",
    temperature=0.6,
    max_tokens=5000
)

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg["content"]}</div>', unsafe_allow_html=True)

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response
    with st.spinner("Thinking..."):
        response = llm.invoke(user_input)

    bot_reply = response.content

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Rerun to update UI
    st.rerun()