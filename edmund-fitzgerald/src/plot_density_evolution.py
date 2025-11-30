# plot_density_evolution.py

import numpy as np
import matplotlib.pyplot as plt
from will_body_surface import will_body_surface


def plot_density_evolution() -> None:
    """
    Visualize how body density changes over time at different depths.
    """
    depths = [10, 50, 100, 162, 200]  # 162m = Edmund Fitzgerald depth
    max_days = 365
    days_range = np.linspace(1, max_days, 100)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot density evolution for each depth
    for depth in depths:
        densities = []
        for days in days_range:
            _, body_dens, water_dens = will_body_surface(depth, days)
            densities.append(body_dens)

        label = f"{depth}m"
        if depth == 162:
            label += " (Edmund Fitz)"
        ax.plot(days_range, densities, label=label, linewidth=2)

    # Add water density reference lines
    ax.axhline(y=1000, color='blue', linestyle='--',
               alpha=0.5, label='Surface water')
    ax.axhline(y=1000.7, color='navy', linestyle='--',
               alpha=0.5, label='Deep water')

    ax.set_xlabel('Days Since Sinking', fontsize=12)
    ax.set_ylabel('Body Density (kg/m³)', fontsize=12)
    ax.set_title('Density Evolution at Different Depths', fontsize=14)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_density_evolution()