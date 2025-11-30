# analyze_edmund_fitzgerald.py

from superior_conditions import superior_conditions
from will_body_surface import will_body_surface

def analyze_edmund_fitzgerald() -> None:
    """
    Analyze the specific case of the Edmund Fitzgerald.
    """
    # Known parameters
    depth = 162  # meters (530 feet)

    print("=" * 60)
    print(" Edmund Fitzgerald Surfacing Analysis")
    print("=" * 60)

    # Check conditions
    conditions = superior_conditions(depth, "November")
    print(f"\nConditions at {depth}m depth:")
    print(f"  Temperature: {conditions.temp_celsius}°C")
    print(f"  Pressure: {conditions.pressure_atm:.1f} atmospheres")
    print(f"  Water density: {conditions.water_density_kg_m3:.1f} kg/m³")

    # Check surfacing probability over time
    print("\nSurfacing probability over time:")

    for days in [7, 30, 90, 180, 365, 365 * 5]:
        will_float, body_dens, _ = will_body_surface(depth, days)

        status = "WILL SURFACE" if will_float else "Remains submerged"
        print(f"  After {days:4d} days: {body_dens:.1f} kg/m³ - {status}")

    # Calculate how much gas would be needed
    print("\nWhat would it take to surface?")

    # Work backwards from buoyancy requirement
    required_density = conditions.water_density_kg_m3 - 1.0
    body_mass = 70.0
    base_density = 985.0

    # Solve for required gas volume
    # density = mass / (mass/base_density + gas_volume)
    required_volume_m3 = (body_mass / required_density) - (body_mass / base_density)
    required_volume_ml = required_volume_m3 * 1e6

    # At pressure
    surface_equivalent_ml = required_volume_ml * conditions.pressure_atm

    print(f"  Required compressed gas: {required_volume_ml:.0f} mL")
    print(f"  Surface equivalent: {surface_equivalent_ml:.0f} mL")
    print(f"  Typical maximum production: {1000 * body_mass:.0f} mL")
    print(f"  Verdict: {'Possible' if surface_equivalent_ml < 1000 * body_mass else 'Impossible'}")

if __name__ == "__main__":
    analyze_edmund_fitzgerald()
