# Sample Code: Hash Collisions and Modern Cryptography

This repository contains the companion code for the blog post:

👉 [Hash Collisions: Why Your 'Unique' Fingerprints Aren't (And Why That's Usually OK)](https://tomarcher.io/posts/hash-collisions/) on [Signal & Syntax](https://tomarcher.io/).

This code demonstrates the mathematical certainty of hash collisions, the near-impossibility of meaningful collisions, and practical implications for modern cryptography. The examples cover everything from the pigeonhole principle and semantic collisions to modern password hashing with Argon2 and blockchain's double SHA-256. The blog post explores how hash functions have evolved from MD5 (broken) through SHA-1 (deprecated) to current best practices with SHA-256/SHA-3 and beyond.

## 📋 Requirements

- [Python 3.10 or 3.11](https://www.python.org/downloads/)
- `pip` for dependency management: `python -m ensurepip --upgrade`

## ⚙️ Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/TomArcher/technical-blog-examples.git
cd technical-blog-examples/hash-collisions
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running the Examples

Run the individual modules in the `src` directory`. The modules copied directly from the post have names that start with "snippet". The modules that don't start with the word "snippet" are enhanced examples meant to explore more detail about the topic.  

```bash
python <module>.py
```

## 📁 What's Included

- **Collision demonstrations** - Proving hash functions aren't unique
- **Semantic collision testing** - Why meaningful collisions are nearly impossible
- **Password hashing evolution** - From MD5+salt to Argon2
- **Modern alternatives** - bcrypt, scrypt, PBKDF2 comparisons
- **Blockchain examples** - Double hashing and crypto-agility patterns
- **Performance benchmarks** - SHA-256 vs Argon2 speed comparisons

## 🤝 Contributing

Pull requests are welcome! If you spot an improvement, bug, or want to extend the examples, feel free to open a PR.
