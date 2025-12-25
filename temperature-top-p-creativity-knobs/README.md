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
pip install -r requirements.txt
```

For API experiments, set your environment variables:

```bash
export OPENAI_API_KEY="your-key-here"
export ANTHROPIC_API_KEY="your-key-here"
```

## 🚀 Running the Examples

Run the simulations and visualizations:

```bash
# Run temperature comparison visualization
python visualize_temperature.py

# Compare top-k vs top-p sampling
python compare_topk_topp.py

# Show temperature and top-p interaction
python temp_topp_interaction.py

# Run API experiments (requires API keys)
python api_experiments.py
```

## 📁 What's Included

### Core Sampling Functions
- **softmax.py** - Standard softmax implementation with numerical stability
- **softmax_with_temperature.py** - Temperature-scaled softmax
- **top_p_sampling.py** - Nucleus sampling implementation
- **top_k_sampling.py** - Fixed top-k sampling for comparison

### Analysis & Comparison
- **compare_topk_topp.py** - Demonstrates when top-p outperforms top-k
- **temp_topp_interaction.py** - Shows how temperature affects nucleus size
- **test_determinism.py** - Tests temperature=0 determinism across providers

### API Experiments
- **api_experiments.py** - Live experiments with OpenAI and Anthropic APIs
- **generate_samples.py** - Generate multiple completions at various settings

### Visualizations
- **visualize_temperature.py** - Bar charts showing probability reshaping
- **plot_entropy_curve.py** - Entropy vs temperature relationship

## 📊 Key Findings

- Temperature divides logits before softmax, exponentially reshaping the distribution
- Low temperature (0.1-0.3) concentrates probability on top tokens
- High temperature (>1.0) flattens toward uniform randomness
- Top-p dynamically adjusts candidate pool based on model confidence
- Temperature applies before top-p, so they interact in non-obvious ways
- Temperature=0 is not perfectly deterministic in all implementations

## 🤝 Contributing

Pull requests are welcome! If you spot an improvement, bug, or want to extend the examples (min-p sampling, repetition penalties, beam search comparisons), feel free to open a PR.