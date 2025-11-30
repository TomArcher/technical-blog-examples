# body_density_with_gas.py

def body_density_with_gas(
        base_density: float,
        gas_volume_ml: float,
        body_mass_kg: float
) -> float:
    """
    Calculate overall body density including gas bubbles.

    Gas reduces overall density by displacing water.

    Args:
        base_density: Initial body density (kg/m³)
        gas_volume_ml: Total gas volume in body (mL)
        body_mass_kg: Total body mass (kg)

    Returns:
        Overall density including gas (kg/m³)
    """
    # Convert mL to m³ (1 mL = 1e-6 m³)
    gas_volume_m3 = gas_volume_ml * 1e-6

    # Calculate base body volume
    body_volume_m3 = body_mass_kg / base_density

    # Total volume = body + gas
    total_volume_m3 = body_volume_m3 + gas_volume_m3

    # Density = mass / volume (gas has negligible mass)
    overall_density = body_mass_kg / total_volume_m3

    return overall_density