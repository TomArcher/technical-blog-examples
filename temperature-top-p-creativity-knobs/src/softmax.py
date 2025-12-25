# softmax.py

import numpy as np

def softmax(logits):
    """Standard softmax: convert logits to probabilities."""
    # Subtract max for numerical stability
    shifted = logits - np.max(logits)
    exp_logits = np.exp(shifted)
    return exp_logits / np.sum(exp_logits)

def main():
    # Example logits for 5 tokens
    logits = np.array([2.0, 1.5, 1.0, 0.5, 0.0])
    probs = softmax(logits)
    print(f"Probabilities: {probs.round(3)}")
    # Output: [0.429 0.26  0.158 0.096 0.058]

if __name__ == "__main__":
    main()