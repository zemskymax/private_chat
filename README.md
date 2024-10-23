# Private Chat

Use Ollama and Streamlit Python libraries to create a private (local) GPT-like chat.

## Overview
This project aims to provide a simple yet powerful tool for creating a local chat interface using the Ollama library and Streamlit. The goal is to enable users to interact with large language models (LLMs) in a conversational manner without relying on cloud-based services.

## Purpose
The primary purpose of this project is to demonstrate the integration of Ollama and Streamlit, showcasing their capabilities in building a user-friendly chat application. Additionally, it serves as a learning resource for those interested in natural language processing and chatbot development.

## Key Features
- **Local Interaction**: The chat runs locally, ensuring data privacy and security.
- **Customizable Model**: Users can choose different LLMs supported by Ollama.
- **Streamlined Setup**: Easy installation and configuration process.
- **Real-time Responses**: Smooth and responsive chat experience.

## Technologies Used
- **Ollama**: A Python library for interacting with large language models.
- **Streamlit**: A Python library for building web applications.

## Problem Solved
This project addresses the need for a secure and private chat solution that leverages advanced NLP techniques. It provides a platform for experimenting with various LLMs and understanding their capabilities in real-world applications.

## Target Audience
- Developers interested in natural language processing and chatbot development.
- Researchers looking to explore the potential of LLMs in local environments.
- Anyone seeking a secure and customizable chat solution.

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
It is required to download the correct LLM via the Ollama before using it. In this example, we use the Llama3 model, which can be downloaded using the following command:
```bash
ollama pull llama3
```

## Usage
```bash
streamlit run main.py
```