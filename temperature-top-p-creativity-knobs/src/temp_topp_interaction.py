# temp_topp_interaction.py

import numpy as np
from softmax_with_temperature import softmax_with_temperature

def temp_topp_interaction():
    """Show how temperature affects top-p token counts."""
    logits = np.random.randn(100) * 2  # 100 tokens
    logits = np.sort(logits)[::-1]  # Sort descending

    temperatures = [0.3, 0.5, 0.7, 1.0, 1.3]
    p = 0.9

    print(f"Tokens included in top-p={p} nucleus at different temperatures:")
    print("-" * 50)

    for T in temperatures:
        probs = softmax_with_temperature(logits, T)
        sorted_probs = np.sort(probs)[::-1]
        cumsum = np.cumsum(sorted_probs)
        tokens_included = np.searchsorted(cumsum, p) + 1
        print(f"  T={T}: {tokens_included} tokens")

if __name__ == "__main__":
    temp_topp_interaction()