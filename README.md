# Gen-AI-Application-Using-DeepSeek-R1-with-Langchain-And-Ollama

A Streamlit application that provides an AI programming assistant using the **DeepSeek-R1** model in combination with **LangChain** and **Ollama**. This project allows you to ask coding questions and receive code snippets, debugging tips, and solution designs in a sleek, dark-themed UI.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Streamlit App](#running-the-app)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [Author](#author)

---

## Overview

**Gen-AI-Application-Using-DeepSeek-R1-with-Langchain-And-Ollama** is an interactive coding assistant built with:
- **Streamlit** for a clean, real-time web interface.
- **DeepSeek-R1** models served locally via **Ollama**.
- **LangChain** for prompt and response management.

Users can ask any coding question, and the AI responds with concise answers, code snippets, or debugging tips.

---

## Features

- **Dark-Themed UI**: Custom CSS to provide a sleek appearance.
- **Model Selection**: Choose between different DeepSeek-R1 models (e.g., `deepseek-r1:1.5b`, `deepseek-r1:3b`).
- **Coding Assistance**: Get Python code snippets, explanations, and debugging strategies.
- **Solution Design**: High-level overviews and architectural advice.

---

## Installation and Setup

### Prerequisites

1. **Python 3.10+** (Recommended)  
   - Check with:  
     ```bash
     python --version
     ```
2. **Ollama** installed and running locally  
   - [Ollama Installation Instructions](https://ollama.ai/docs/install)
   - Make sure Ollama is serving on [http://localhost:11434](http://localhost:11434) (default port).
3. **Git** (if you plan to clone from GitHub)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pahul1712/Gen-AI-Application-Using-DeepSeek-R1-with-Langchain-And-Ollama.git


### Install Dependencies:

```bash
  pip install -r requirements.txt


### Running the Streamlit App:

```bash
  streamlit run app.py



## File Structure 
Gen-AI-Application-Using-DeepSeek-R1-with-Langchain-And-Ollama/
├── app.py                # Main Streamlit application
├── README.md             # Project documentation (you're reading it now)
├── requirements.txt      # All Python dependencies
├── test.py               # Example or placeholder test script
├── .gitignore            # Git ignore file
└── venv/                 # (Optional) Virtual environment folder


1. app.py:
Contains the Streamlit code, UI design, and LLM prompt logic.

2. requirements.txt:
Lists dependencies needed to run the app.

3. test.py:
Basic script for testing or demonstration.


### Contributing

1. Fork the repository
2. Create a new branch for your feature/fix:
     git checkout -b feature/my-new-feature
     git commit -m "Add some feature"
     git push origin feature/my-new-feature
     
### Author

Pahuldeep Singh Dhingra [ MS in Data Science at Florida Atlantic University,FL,USA]
Check out my GitHub (@pahul1712) for more projects!

Can also reach out to me on other plarforms:

1. LinkedIn:  https://www.linkedin.com/in/pahuldeepsing/
2. Personal Email: pahuldeepSingh531@gmail.com






