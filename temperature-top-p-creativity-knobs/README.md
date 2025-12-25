# Sample Code: Temperature and Top-P - The Creativity Knobs

This repository contains the companion code for the blog post:

👉 [Temperature and Top-P: The Creativity Knobs](https://tomarcher.io/posts/temperature-top-p-creativity-knobs/) on [Signal & Syntax](https://tomarcher.io/).

This code demonstrates the mathematics behind LLM sampling parameters. The examples show how temperature reshapes probability distributions via softmax scaling, how nucleus (top-p) sampling dynamically truncates token candidates, and how these parameters interact when used together. The blog post includes working implementations, visualizations, and practical experiments with OpenAI and Anthropic APIs.

## 📋 Requirements

- [Python 3.10 or 3.11](https://www.python.org/downloads/)
- `pip` for dependency management: `python -m ensurepip --upgrade`
- `matplotlib` for visualizations
- `numpy` for numerical computations
- `openai` for OpenAI API experiments (optional)
- `anthropic` for Anthropic API experiments (optional)

## ⚙️ Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/TomArcher/technical-blog-examples.git
cd technical-blog-examples/temperature-top-p-creativity-knobs
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

For API experiments, set your environment variables:

```bash
export OPENAI_API_KEY="your-key-here"
export ANTHROPIC_API_KEY="your-key-here"
```

## 🚀 Running the Examples

Run the simulations and visualizations:

**softmax.py** — Converts raw logits into probabilities that sum to 1 using the standard softmax function.

**softmax_with_temperature.py**: Applies temperature scaling to logits before softmax, reshaping the probability distribution.

**visualize_temperature_effects.py**: Generates bar charts comparing probability distributions across different temperature values.

**top_p_sampling.py**: Implements nucleus sampling by dynamically truncating the distribution to tokens summing to probability p.

**compare_topk_topp.py**: Demonstrates why top-p outperforms top-k by comparing token inclusion in confident vs uncertain distributions.

**temp_topp_interaction.py**: Shows how temperature affects the number of tokens that survive a top-p cutoff.

**openai_generate.py**: Generates multiple completions using the OpenAI API with configurable temperature and top-p parameters.

**anthropic_generate.py**: Generates multiple completions using the Anthropic API with configurable temperature and top-p parameters.

**test_determinism.py**: Tests whether temperature=0 produces identical outputs across multiple trials.

## 🤝 Contributing

Pull requests are welcome! If you spot an improvement, bug, or want to extend the examples (min-p sampling, repetition penalties, beam search comparisons), feel free to open a PR.