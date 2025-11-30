# gas_production_model.py

import math
from decomposition_rate import decomposition_rate

def gas_production_model(
        days: float,
        temp_celsius: float,
        body_mass_kg: float = 70.0
) -> float:
    """
    Calculate cumulative gas production from decomposition.

    Assumes exponential approach to maximum gas production.
    Complete decomposition produces ~1000 mL gas per kg body mass.

    Args:
        days: Time since death (days)
        temp_celsius: Water temperature
        body_mass_kg: Body mass in kg

    Returns:
        Total gas produced (mL)
    """
    # Get temperature-adjusted decomposition rate
    rate = decomposition_rate(temp_celsius)

    # Maximum possible gas (mL)
    max_gas = 1000.0 * body_mass_kg

    # Exponential approach to maximum
    # Gas = max * (1 - e^(-rate * time))
    gas_produced = max_gas * (1 - math.exp(-rate * days))

    return gas_produced
