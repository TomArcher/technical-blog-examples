import numpy as np
import matplotlib.pyplot as plt

def attention_weights(context_length, query_position):
    positions = np.arange(context_length)
    recency = np.exp(-0.001 * (query_position - positions))
    distance_penalty = 1.0 / (1.0 + 0.00001 * (query_position - positions)**2)
    weights = recency * distance_penalty
    weights = weights / weights.sum()
    return weights

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for idx, ctx_len in enumerate([1000, 10000, 100000]):
    query_pos = ctx_len - 1
    weights = attention_weights(ctx_len, query_pos)
    axes[idx].plot(weights)
    axes[idx].set_title(f'Context Length: {ctx_len:,} tokens')
    axes[idx].set_xlabel('Token Position')
    axes[idx].set_ylabel('Attention Weight')
    axes[idx].set_yscale('log')
plt.tight_layout()
plt.show()