# Gen-AI-Application-Using-DeepSeek-R1-with-Langchain-And-Ollama

A Streamlit application that provides an AI programming assistant using the **DeepSeek-R1** model in combination with **LangChain** and **Ollama**. This project allows you to ask coding questions and receive code snippets, debugging tips, and solution designs in a sleek, dark-themed UI.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [Usage](#usage)
  - [Example Queries](#example-queries)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
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

