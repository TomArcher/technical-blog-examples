# validate_historical_disasters.py

from will_body_surface import will_body_surface

def validate_historical_disasters() -> None:
    """
    Compare model predictions against known outcomes from maritime disasters.
    """
    disasters = [
        # (Name, Depth_m, Temp_C, Days_to_recovery, Bodies_recovered)
        ("Titanic (1912)", 3800, 2, None, False),
        ("Lusitania (1915)", 93, 9, 14, True),
        ("Andrea Doria (1956)", 75, 12, 7, True),
        ("Estonia (1994)", 85, 4, None, False),
    ]

    print("\nHistorical Disaster Validation:")
    print("=" * 60)

    for name, depth, temp, actual_days, recovered in disasters:
        # Run our model
        if actual_days:
            will_float, _, _ = will_body_surface(depth, actual_days)
        else:
            # Check if ever possible
            will_float = False
            for days in range(1, 365):
                floats, _, _ = will_body_surface(depth, days)
                if floats:
                    will_float = True
                    break

        # Compare to historical record
        model_predicts = "Surface" if will_float else "No surface"
        actual_result = "Recovered" if recovered else "Not recovered"
        match = "✓" if (will_float == recovered) else "✗"

        print(f"\n{name}")
        print(f"  Depth: {depth}m, Temp: {temp}°C")
        print(f"  Model: {model_predicts}")
        print(f"  Actual: {actual_result} {match}")

if __name__ == "__main__":
    validate_historical_disasters()