# gas_volume_at_depth.py

def gas_volume_at_depth(surface_volume_ml: float, depth_meters: float) -> float:
    """
    Calculate compressed gas volume at depth using Boyle's Law.

    Pressure increases by 1 atmosphere every 10 meters.
    Gas volume inversely proportional to pressure.

    Args:
        surface_volume_ml: Gas volume at surface pressure (mL)
        depth_meters: Depth below surface (meters)

    Returns:
        Compressed gas volume at depth (mL)
    """
    # Calculate absolute pressure (atmospheres)
    pressure_atm = 1.0 + (depth_meters / 10.0)

    # Boyle's Law: P1V1 = P2V2
    compressed_volume = surface_volume_ml / pressure_atm

    return compressed_volume