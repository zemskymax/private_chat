# private_chat
Use Ollama and Streamlit Python libraries to create a private (local) GPT like chat.

# Installation
pip install ollama
** Test **
ollama -v

pip install streamlit
** Test **
streamlit hello

# Important
It is required to download the correct LLM via the Ollama before using it.
In this example we use the Llama3 model, to download it use the following command:
ollama pull llama3

# Usage 
streamlit run main.py
