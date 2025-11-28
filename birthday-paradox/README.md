# Sample Code: The Birthday Paradox in Production

This repository contains the companion code for the blog post:

👉 [The Birthday Paradox in Production: When Random IDs Collide](https://tomarcher.io/posts/birthday-paradox/) on [Signal & Syntax](https://tomarcher.io/).

This code demonstrates how the birthday paradox affects real-world ID generation systems, from 32-bit integers to UUID v4. The examples calculate collision probabilities, validate with Monte Carlo simulations, and visualize why your "guaranteed unique" database IDs collide far sooner than intuition suggests. The blog post explores how collision probability grows quadratically (not linearly), why a trillion-value space becomes risky at just one million items, and provides practical guidance for choosing between 32-bit, 64-bit, and UUID systems.

## 📋 Requirements

- [Python 3.10 or 3.11](https://www.python.org/downloads/)
- `pip` for dependency management: `python -m ensurepip --upgrade`
- `matplotlib` and `numpy` for visualizations

## ⚙️ Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/TomArcher/technical-blog-examples.git
cd technical-blog-examples/birthday-paradox
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running the Examples

Run the main analysis script to see all demonstrations:

```bash
python main.py
```

Or run individual modules:

```bash
python exact_collision_probability.py
python collision_threshold.py
python collision_scenario.py
```

## 📁 What's Included

- **Probability calculations** - Exact and approximate collision probability formulas
- **Threshold analysis** - Find when you'll hit specific risk levels (1%, 50%, 99%)
- **Monte Carlo validation** - Simulate millions of trials to verify the math
- **Production scenarios** - Real-world analysis from startup MVPs to distributed logs
- **ID system comparison** - 32-bit vs 64-bit vs UUID v4 collision resistance
- **Interactive visualizations** - Log-scale plots showing when different systems fail
- **Time-to-collision charts** - How long until failure at various generation rates

## 📊 Key Findings

At 1 billion IDs/second:
- **32-bit**: Collides in 77 microseconds
- **64-bit**: Collides in 1.4 hours  
- **UUID v4**: Collides in 86 years

## 🤝 Contributing

Pull requests are welcome! If you spot an improvement, bug, or want to extend the examples, feel free to open a PR.
