import streamlit as st
import ollama


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

options = {
    'num_ctx': 4096, # default is 2048
    'temperature': 0.2, # default is 0.8
    'top_k': 15, # default is 40
    'top_p': 0.5, #default is 0.9
}

## Generate a response (async) using an LLM
def generate_response():
    response = ollama.chat(model='llama3', stream=True, messages=st.session_state.messages, options=options)
    for partial_resp in response:
        try:
            token = partial_resp["message"]["content"]
            st.session_state["full_message"] += token
            yield token
        except Exception as inst:
            print("---> " + inst)


# Handle user input
if prompt := st.chat_input("Enter your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)
    
    # Clear the previous message
    st.session_state["full_message"] = ""
    
    # Write the generated response
    st.chat_message("assistant", avatar="🤖").write_stream(generate_response)

    # Update message history
    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})