# decomposition_rate.py

import math

def decomposition_rate(temp_celsius: float, baseline_rate: float = 0.15) -> float:
    """
    Calculate decomposition rate at given temperature using Q10 coefficient.

    Q10 ≈ 2.5 means rate increases 2.5x for every 10°C increase.
    Baseline rate is calibrated for 20°C (Gillooly et al., 2001).

    Args:
        temp_celsius: Water temperature in Celsius
        baseline_rate: Decomposition rate at 20°C (fraction per day)

    Returns:
        Adjusted decomposition rate (fraction per day)
    """
    Q10 = 2.5  # Temperature coefficient for biological processes
    temp_diff = temp_celsius - 20.0  # Difference from reference temp

    # Q10 equation: rate = baseline * Q10^(ΔT/10)
    rate_multiplier = Q10 ** (temp_diff / 10.0)

    return baseline_rate * rate_multiplier