# will_body_surface.py

from typing import Tuple
from superior_conditions import superior_conditions
from gas_volume_at_depth import gas_volume_at_depth
from gas_production_model import gas_production_model
from body_density_with_gas import body_density_with_gas

def will_body_surface(
        depth_meters: float,
        days_elapsed: float,
        body_mass_kg: float = 70.0,
        base_density: float = 985.0
) -> Tuple[bool, float, float]:
    """
    Determine if body will surface given conditions and time.

    Args:
        depth_meters: Depth of body
        days_elapsed: Time since death
        body_mass_kg: Mass of body
        base_density: Initial body density (kg/m³)

    Returns:
        Tuple of (will_float, body_density, water_density)
    """
    # Get environmental conditions
    conditions = superior_conditions(depth_meters)

    # Calculate gas production at this temperature
    gas_ml = gas_production_model(
        days_elapsed,
        conditions.temp_celsius,
        body_mass_kg
    )

    # Compress gas to depth pressure
    compressed_gas_ml = gas_volume_at_depth(gas_ml, depth_meters)

    # Calculate overall density with gas
    body_density = body_density_with_gas(
        base_density,
        compressed_gas_ml,
        body_mass_kg
    )

    # Will float if less dense than water
    will_float = body_density < conditions.water_density_kg_m3

    return will_float, body_density, conditions.water_density_kg_m3
