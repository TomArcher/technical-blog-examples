# plot_surfacing_zones.py

import numpy as np
import matplotlib.pyplot as plt
from will_body_surface import will_body_surface

def plot_surfacing_zones() -> None:
    """
    Create contour map showing zones where bodies will surface vs remain submerged.
    """
    max_days = 365
    # Focus on shallower depths where the transition actually happens
    depths_grid = np.linspace(0, 120, 60)  # Reduced max depth to 120m
    days_grid = np.linspace(1, max_days, 50)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Calculate surfacing probability for each depth/time combination
    will_surface = np.zeros((len(depths_grid), len(days_grid)))

    for i, depth in enumerate(depths_grid):
        for j, days in enumerate(days_grid):
            will_float, _, _ = will_body_surface(depth, days)
            will_surface[i, j] = float(will_float)

    # Create contour plot with better color contrast
    contour = ax.contourf(days_grid, depths_grid, will_surface,
                          levels=[0, 0.5, 1],
                          colors=['darkblue', 'lightblue'],
                          extend='both')
    ax.invert_yaxis()  # Depth increases downward

    # Add contour lines to make the boundary clearer
    ax.contour(days_grid, depths_grid, will_surface,
               levels=[0.5], colors='white', linewidths=2)

    # Mark the Edmund Fitzgerald depth (will be off the chart if we use 120m max)
    ax.axhline(y=120, color='red', linestyle='--',
               linewidth=2, label='Edmund Fitzgerald at 162m (below chart)')

    ax.set_xlabel('Days Since Sinking', fontsize=12)
    ax.set_ylabel('Depth (meters)', fontsize=12)
    ax.set_title('Surfacing Zones in Lake Superior\n(Light = Will Surface, Dark = Remains Submerged)', fontsize=14)
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_surfacing_zones()