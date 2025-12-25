# softmax_with_temperature.py

import numpy as np
import matplotlib.pyplot as plt

def softmax_with_temperature(logits, temperature):
    """Apply temperature scaling before softmax."""
    if temperature == 0:
        # Greedy: return one-hot for max logit
        result = np.zeros_like(logits)
        result[np.argmax(logits)] = 1.0
        return result
    scaled = logits / temperature
    shifted = scaled - np.max(scaled)
    exp_logits = np.exp(shifted)
    return exp_logits / np.sum(exp_logits)

def main():
    # Same logits, different temperatures
    logits = np.array([2.0, 1.5, 1.0, 0.5, 0.0])
    temperatures = [0.1, 0.5, 1.0, 1.5, 2.0]

    print("Token probabilities at different temperatures:")
    print("-" * 50)
    for T in temperatures:
        probs = softmax_with_temperature(logits, T)
        entropy = -np.sum(probs * np.log(probs + 1e-10))
        print(f"T={T:.1f}: {probs.round(3)} | Entropy: {entropy:.2f}")

if __name__ == "__main__":
    main()