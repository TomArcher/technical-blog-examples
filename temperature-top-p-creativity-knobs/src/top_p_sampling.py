# top_p_sampling

import numpy as np
from softmax_with_temperature import softmax_with_temperature

def top_p_sampling(logits, p, temperature=1.0):
    """Apply nucleus (top-p) sampling."""
    # First apply temperature
    probs = softmax_with_temperature(logits, temperature)

    # Sort by probability
    sorted_indices = np.argsort(probs)[::-1]
    sorted_probs = probs[sorted_indices]

    # Find cumulative sum
    cumsum = np.cumsum(sorted_probs)

    # Find cutoff index (first index where cumsum >= p)
    cutoff_idx = np.searchsorted(cumsum, p) + 1

    # Create mask
    mask = np.zeros_like(probs)
    mask[sorted_indices[:cutoff_idx]] = 1

    # Apply mask and renormalize
    masked_probs = probs * mask
    return masked_probs / np.sum(masked_probs)

def main():
    # Example
    logits = np.array([3.0, 2.5, 2.0, 1.0, 0.5, 0.0, -0.5, -1.0])
    tokens = ['the', 'a', 'one', 'some', 'that', 'this', 'an', 'my']

    print("Original probabilities:")
    orig_probs = softmax_with_temperature(logits, 1.0)
    for tok, prob in zip(tokens, orig_probs):
        print(f"  {tok}: {prob:.3f}")

    print(f"\nAfter top-p=0.9:")
    nucleus_probs = top_p_sampling(logits, p=0.9, temperature=1.0)
    for tok, prob in zip(tokens, nucleus_probs):
        if prob > 0:
            print(f"  {tok}: {prob:.3f}")

if __name__ == "__main__":
    main()