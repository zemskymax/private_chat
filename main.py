import streamlit as st

# Set page title
st.session_state.app_name = "⚡️ Private Chat"
st.title(f"{st.session_state.app_name}")

# Add BOT (LLM) greeting (if needed)
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi There, how can I help you?"}]

# Write message history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

# Handle user input
if prompt := st.chat_input("Enter your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)
    with st.chat_message("assistant", avatar="🤖"):
        response = "I can hear this - " + prompt
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})