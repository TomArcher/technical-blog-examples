# Sample Code: How Large Language Models (LLMs) Handle Context Windows: The Memory That Isn't Memory

This repository contains the companion code for the blog post:
👉 [How Large Language Models (LLMs) Handle Context Windows: The Memory That Isn't Memory](https://tomarcher.io/posts/how-large-language-models-handle-context-windows/) on [Signal & Syntax](https://tomarcher.io/).

## 📚 What This Code Demonstrates

This code provides a conceptual Python implementation showing how attention mechanisms work in Large Language Models, with a focus on how attention weights distribute across growing contexts. Through visual demonstrations, you'll see:

- **Attention weight distribution** - How each token "attends to" or focuses on other tokens in the sequence
- **The quadratic scaling problem** - Why doubling context length quadruples computational cost
- **Lost in the middle phenomenon** - How information buried in long contexts gets lower attention weights
- **Recency bias** - Why models often focus more on the beginning and end of long contexts
- **Memory illusion** - How attention creates the appearance of memory without actual state retention
- **Context window limitations** - What happens as sequences approach maximum length

The visualization helps demystify why LLMs can seem to "remember" conversation history while actually performing stateless computation on the entire context for each response. This conceptual model mirrors the attention patterns found in transformer-based models like GPT-4 and Claude.

## 📋 Requirements
- [Python 3.10 or 3.11](https://www.python.org/downloads/)
- `pip` for dependency management: `python -m ensurepip --upgrade`

## ⚙️ Setup
Clone the repo and install dependencies:
```bash
git clone https://github.com/TomArcher/technical-blog-examples.git
cd technical-blog-examples/how-large-language-models-handle-context-windows
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running the Sample
Run the main script:
```bash
python main.py
```

## 🤝 Contributing
Pull requests are welcome! If you spot an improvement, bug, or want to extend the sample, feel free to open a PR.
