# Sample Code: How Large Language Models Tokenize Text: Why Words Aren't What You Think

This repository contains the companion code for the blog post:
👉 [How Large Language Models Tokenize Text: Why Words Aren't What You Think](https://tomarcher.io/posts/how-large-language-models-tokenize-text/) on [Signal & Syntax](https://tomarcher.io/).

## 📚 What This Code Demonstrates

This code provides hands-on examples of how Large Language Models tokenize text using OpenAI's `tiktoken` library. Through practical demonstrations, you'll see:

- **Token counting in action** - How the same GPT-4 tokenizer used by the OpenAI API breaks down text into tokens
- **Why tokens ≠ words** - Common phrases tokenize differently than you'd expect
- **Efficiency variations** - How common words use fewer tokens than rare words
- **Language differences** - Why non-English text often requires more tokens
- **Code tokenization** - How programming code splits differently than natural language
- **Character-level blindness** - Why LLMs struggle with tasks like counting letters in "strawberry"

The examples mirror those from the blog post, allowing you to experiment with your own text and see firsthand how tokenization affects API costs, context window usage, and model behavior.

## 📋 Requirements
- [Python 3.10 or 3.11](https://www.python.org/downloads/)
- `pip` for dependency management: `python -m ensurepip --upgrade`

## ⚙️ Setup
Clone the repo and install dependencies:
```bash
git clone https://github.com/TomArcher/technical-blog-examples.git
cd technical-blog-examples/how-large-language-models-tokenize-text
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
