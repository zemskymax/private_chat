# Private Chat

## Overview

This project uses Ollama and Streamlit Python libraries to create a private (local) GPT-like chat application. It allows users to interact with large language models (LLMs) in a conversational manner without relying on cloud-based services.

## Purpose

The primary goal of this project is to demonstrate how to build a local chat interface using Ollama and Streamlit. This can be useful for those who want to explore the capabilities of LLMs in a secure and controlled environment.

## Key Features

- **Local Interaction**: Interact with LLMs locally, ensuring data privacy and security.
- **Customizable Settings**: Adjust settings such as context length, temperature, top-k, and top-p to fine-tune the chat experience.
- **Streamlined Setup**: Easy-to-follow instructions for setting up and running the application.

## Technologies Used

- [Ollama](https://ollama.com/): A platform for managing and interacting with LLMs.
- [Streamlit](https://streamlit.io/): An open-source app framework for ML and data teams.

## Installation

### Prerequisites

Before installing the dependencies, ensure you have Python installed on your system.

#### Install Ollama
```bash
pip install ollama
```

#### Verify Installation
```bash
ollama -v
```

### Dependencies

Install the necessary dependencies using pip.
```bash
pip install streamlit
```

#### Verify Installation
```bash
streamlit hello
```

## Important Notes

It is essential to download the appropriate LLM via Ollama before using it. In this example, we use the Llama3 model. To download it, run the following command:
```bash
ollama pull llama3
```

## Usage

Run the application using the following command:
```bash
streamlit run main.py
```