# private_chat

## Overview

Use Ollama and Streamlit Python libraries to create a private (local) GPT-like chat application.

## Purpose

This project aims to provide a simple yet powerful tool for creating a local chat interface using advanced language models. The goal is to enable users to interact with large language models in a conversational manner without relying on cloud-based services.

## Key Features

- **Local Interaction**: No internet connection required; all interactions happen locally.
- **Customizable Model**: Supports downloading various language models through Ollama, allowing flexibility in choosing the desired model.
- **Streamlit Interface**: A user-friendly web interface built with Streamlit for easy interaction.

## Technologies Used

- [Ollama](https://ollama.com/): A platform for managing and interacting with large language models.
- [Streamlit](https://streamlit.io/): An open-source app framework for Python that makes it easy to build beautiful, custom web apps.

## Problem Solved

This project addresses the need for a secure and efficient way to interact with AI models locally, ensuring privacy and control over data.

## Target Audience

- Developers looking to integrate advanced NLP capabilities into their applications.
- Researchers interested in experimenting with different language models.
- Individuals who value privacy and want to avoid cloud-based solutions.

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

It is required to download the correct LLM via Ollama before using it. In this example, we use the Llama3 model, which can be downloaded using the following command:

```bash
ollama pull llama3
```

## Usage

```python
# Run the application
streamlit run main.py
```