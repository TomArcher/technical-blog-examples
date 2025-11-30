# lake_conditions.py

from dataclasses import dataclass

@dataclass
class LakeConditions:
    """Environmental conditions at specific depth in lake."""
    depth_meters: float
    temp_celsius: float
    pressure_atm: float
    water_density_kg_m3: float