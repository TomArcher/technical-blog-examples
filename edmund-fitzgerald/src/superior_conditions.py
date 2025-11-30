# superior_conditions.py

import math
from lake_conditions import LakeConditions

def superior_conditions(depth_meters: float, season: str = "November") -> LakeConditions:
    """
    Model Lake Superior conditions at given depth.

    Superior has thermocline around 60-200 feet.
    Below 60 meters, temperature constant at 4°C year-round.
    November conditions assume late fall (storm season).

    Args:
        depth_meters: Depth below surface
        season: Time of year (affects surface temp only)

    Returns:
        Environmental conditions at depth
    """
    # Temperature profile
    if depth_meters < 60:
        # Surface layer - seasonal variation
        if season == "November":
            temp = 8.0  # Cold but not frozen
        else:
            temp = 4.0 + (16.0 * math.exp(-depth_meters / 30))
    else:
        # Below thermocline - constant 4°C
        temp = 4.0

    # Pressure increases linearly with depth
    pressure = 1.0 + (depth_meters / 10.0)

    # Water density increases with depth (freshwater)
    # Base density ~1000 kg/m³, increases ~0.0044 kg/m³ per meter
    water_density = 1000.0 + (depth_meters * 0.0044)

    return LakeConditions(
        depth_meters=depth_meters,
        temp_celsius=temp,
        pressure_atm=pressure,
        water_density_kg_m3=water_density
    )