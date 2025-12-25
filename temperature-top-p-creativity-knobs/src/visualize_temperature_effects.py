# visualize_temperature_effects.py

import numpy as np
import matplotlib.pyplot as plt
from softmax_with_temperature import softmax_with_temperature

def visualize_temperature_effects():
    """Show how temperature reshapes probability distributions."""
    # Simulate logits for 20 tokens (sorted for visualization)
    np.random.seed(42)
    logits = np.sort(np.random.randn(20) * 2)[::-1]

    temperatures = [0.3, 0.7, 1.0, 1.5]

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    for ax, T in zip(axes, temperatures):
        probs = softmax_with_temperature(logits, T)
        bars = ax.bar(range(20), probs, color='steelblue', alpha=0.7)

        # Highlight top token
        bars[0].set_color('darkred')

        ax.set_title(f'Temperature = {T}', fontsize=14)
        ax.set_xlabel('Token rank')
        ax.set_ylabel('Probability')
        ax.set_ylim(0, max(probs) * 1.1)

        # Annotate top probability
        ax.annotate(f'{probs[0]:.1%}', xy=(0, probs[0]),
                    xytext=(2, probs[0]), fontsize=10)

    plt.tight_layout()
    plt.savefig('temperature_comparison.png', dpi=150)
    plt.show()

if __name__ == "__main__":
    visualize_temperature_effects()