# Private Chat

Use Ollama and Streamlit Python libraries to create a private (local) GPT-like chat.

## Overview
This project aims to provide a simple yet powerful tool for creating a private chat environment using the Ollama library and Streamlit. The chat is built around a large language model (LLM), which can be customized based on your needs.

## Installation
```bash
pip install ollama
# Test
ollama -v

pip install streamlit
# Test
streamlit hello
``` 

## Important
It is required to download the correct LLM via the Ollama before using it. In this example, we use the Llama3 model, to download it use the following command:
```bash
ollama pull llama3
``` 

## Usage
```bash
streamlit run main.py
```