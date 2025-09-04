# Sample Code: The Five-Second Rule Explored with Math & Python

This repository contains the companion code for the blog post:

👉 [The Five-Second Rule, Debunked with Math and Python](https://tomarcher.io/posts/five-second-rule/) on [Signal & Syntax](https://tomarcher.io/).

This code demonstrates how to model food contamination when dropped on the floor. Instead of treating the "five-second rule" as a binary yes/no question, the simulation shows how germs transfer over time based on surface contamination, food contact area, and food properties like moisture and texture. The blog post walks through the logic, math modeling, AI prompts, and lessons learned. This sample provides the runnable Python code behind that exploration.

## 📋 Requirements

- [Python 3.10 or 3.11](https://www.python.org/downloads/)
- `pip` for dependency management: `python -m ensurepip --upgrade`

## ⚙️ Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/TomArcher/technical-blog-examples.git
cd technical-blog-examples/five-second-rule
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
