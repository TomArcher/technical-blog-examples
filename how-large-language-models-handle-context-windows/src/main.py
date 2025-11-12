import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 6))

# Define use cases with token ranges (log scale for visualization)
use_cases = [
    # Short context
    ('Code completion', 100, 1000, 'green'),
    ('Customer service', 1000, 10000, 'green'),
    ('Translation', 1000, 10000, 'green'),
    
    # Long context valuable
    ('Document analysis', 10000, 100000, 'blue'),
    ('Long conversations', 10000, 100000, 'blue'),
    ('Codebase understanding', 50000, 200000, 'blue'),
    
    # Long context problematic
    ('Cross-document reasoning', 100000, 1000000, 'orange'),
    ('Fact extraction (large)', 100000, 1000000, 'orange'),
    ('Long-term state', 100000, 1000000, 'orange'),
]

# Extract data
labels = [uc[0] for uc in use_cases]
mins = [uc[1] for uc in use_cases]
maxs = [uc[2] for uc in use_cases]
colors = [uc[3] for uc in use_cases]

# Create horizontal bars
y_pos = np.arange(len(labels))
widths = [max_val - min_val for min_val, max_val in zip(mins, maxs)]

ax.barh(y_pos, widths, left=mins, color=colors, alpha=0.7, height=0.6)

# Formatting
ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.set_xlabel('Context Window Size (tokens)', fontsize=12)
ax.set_xscale('log')
ax.set_xlim(50, 2000000)
ax.grid(axis='x', alpha=0.3, linestyle='--')

# Add vertical lines for common model limits
ax.axvline(128000, color='gray', linestyle=':', alpha=0.5, linewidth=1.5)
ax.text(128000, len(labels), 'GPT-4\n128K', ha='center', va='bottom', 
        fontsize=9, color='gray')

ax.axvline(200000, color='gray', linestyle=':', alpha=0.5, linewidth=1.5)
ax.text(200000, len(labels), 'Claude 3\n200K', ha='center', va='bottom', 
        fontsize=9, color='gray')

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='green', alpha=0.7, label='Short context sufficient'),
    Patch(facecolor='blue', alpha=0.7, label='Long context valuable'),
    Patch(facecolor='orange', alpha=0.7, label='Long context problematic')
]
ax.legend(handles=legend_elements, loc='lower right')

ax.set_title('Context Window Requirements by Use Case', 
             fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('context-use-cases.png', dpi=300, bbox_inches='tight')
plt.show()