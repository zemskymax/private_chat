# Private Chat

Use Ollama and Streamlit Python libraries to create a private (local) GPT-like chat.

## Overview
This project aims to provide a simple yet powerful tool for creating a local chat interface using the Ollama library and Streamlit. The goal is to enable users to interact with large language models (LLMs) in a conversational manner without relying on cloud-based services.

## Purpose
The primary purpose of this project is to demonstrate how to integrate Ollama and Streamlit to build a private chat application. It serves as a learning resource for those interested in building similar applications or exploring the capabilities of LLMs locally.

## Key Features
- **Local Interaction**: Interact with LLMs directly on your machine.
- **Streamlit Interface**: A user-friendly interface built with Streamlit.
- **Customizable Settings**: Adjust settings like context length, temperature, top-k, and top-p.
- **Easy Setup**: Simple installation instructions and a quick start guide.

## Technologies Used
- [Ollama](https://github.com/olammanai/ollama): A Python library for interacting with LLMs.
- [Streamlit](https://streamlit.io/): An open-source app framework for Python.

## Problem Solved
This project addresses the need for a local, self-hosted solution for interacting with LLMs. By leveraging Ollama and Streamlit, users can have full control over their interactions with these models, ensuring privacy and security.

## Target Audience
- Developers looking to experiment with LLMs in a local environment.
- Researchers interested in building custom chat interfaces.
- Anyone curious about integrating advanced AI into their projects.

## Installation
```bash
pip install ollama
```
**Test:**
```bash
ollama -v
```

```bash
pip install streamlit
```
**Test:**
```bash
streamlit hello
```

## Important
It is required to download the correct LLM via Ollama before using it. In this example, we use the Llama3 model, which can be downloaded using the following command:
```bash
ollama pull llama3
```

## Usage
```bash
streamlit run main.py
```

## Screenshots
![](https://via.placeholder.com/600x400?text=Screenshots+will+go+here)

## Contributing
Contributions are welcome! Please refer to the [contributing guidelines](CONTRIBUTING.md) for details on how to contribute to the project.

## Credits
- [Ollama GitHub Repository](https://github.com/olammanai/ollama)
- [Streamlit GitHub Repository](https://github.com/streamlit/streamlit)