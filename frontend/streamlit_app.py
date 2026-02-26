import streamlit as st
import requests
import base64

# ----------------------------
# CONFIG
# ----------------------------

BACKEND_URL = "https://titanic-chat-agent-backend.onrender.com/"  # change when deploying

st.set_page_config(
    page_title="Titanic AI Data Analyst",
    page_icon="🚢",
    layout="centered"
)

st.title("🚢 Titanic AI Data Analyst")
st.markdown("Ask questions about the Titanic dataset in natural language.")

# ----------------------------
# SESSION STATE
# ----------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------
# USER INPUT
# ----------------------------

st.markdown("### Try asking:")
st.markdown("- What percentage of passengers survived?")
st.markdown("- Show histogram of passenger ages")
st.markdown("- What was the average ticket fare?")



user_input = st.chat_input("Ask something about the Titanic dataset...")

if user_input:
    # Save user message
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    # Call backend
    with st.spinner("Analyzing..."):
        try:
            response = requests.post(
                BACKEND_URL,
                json={"message": user_input},
                timeout=60
            )
            data = response.json()
        except Exception as e:
            data = {
                "answer": f"Backend connection error: {str(e)}",
                "image": None
            }

    # Save assistant response
    st.session_state.chat_history.append({
        "role": "assistant",
        "answer": data.get("answer"),
        "image": data.get("image")
    })

# ----------------------------
# RENDER CHAT
# ----------------------------

for message in st.session_state.chat_history:

    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])

    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message["answer"])

            if message.get("image"):
                st.image(
                    base64.b64decode(message["image"]),
                    width=800
                )
if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history = []

    st.rerun()
