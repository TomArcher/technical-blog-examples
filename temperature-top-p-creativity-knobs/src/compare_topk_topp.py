# compare_topk_topp.py

import numpy as np
from softmax_with_temperature import softmax_with_temperature

def compare_topk_topp():
    """Demonstrate when top-p outperforms top-k."""

    # Scenario A: Confident model
    confident_logits = np.array([5.0, 2.0, 1.0, 0.0, -1.0, -2.0, -3.0, -4.0])

    # Scenario B: Uncertain model
    uncertain_logits = np.array([1.0, 0.95, 0.9, 0.85, 0.8, 0.3, 0.25, 0.2])

    for name, logits in [("Confident", confident_logits),
                         ("Uncertain", uncertain_logits)]:
        probs = softmax_with_temperature(logits, 1.0)
        sorted_idx = np.argsort(probs)[::-1]
        sorted_probs = probs[sorted_idx]

        # Top-k=3
        topk_included = 3
        topk_mass = np.sum(sorted_probs[:topk_included])

        # Top-p=0.9
        cumsum = np.cumsum(sorted_probs)
        topp_included = np.searchsorted(cumsum, 0.9) + 1

        print(f"{name} model:")
        print(f"  Top-k=3: includes {topk_included} tokens, "
              f"captures {topk_mass:.1%} of mass")
        print(f"  Top-p=0.9: includes {topp_included} tokens, "
              f"captures 90% of mass")
        print()

if __name__ == "__main__":
    compare_topk_topp()
