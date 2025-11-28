# main.py

from collision_scenario import CollisionScenario
from id_system import IDSystem
from exact_collision_probability import exact_collision_probability
from collision_threshold import collision_simulator, find_collision_threshold

def analyze_production_systems() -> None:
    """Analyze collision risk in realistic scenarios"""

    scenarios = [
        CollisionScenario(
            "Startup MVP (32-bit IDs, 1K users/day)",
            IDSystem.INT32,
            current_items=10_000,
            growth_rate=1_000
        ),
        CollisionScenario(
            "Growing SaaS (64-bit IDs, 100K users/day)",
            IDSystem.INT64,
            current_items=10_000_000,
            growth_rate=100_000
        ),
        CollisionScenario(
            "Social Platform (64-bit IDs, 10M posts/day)",
            IDSystem.INT64,
            current_items=1_000_000_000,
            growth_rate=10_000_000
        ),
        CollisionScenario(
            "Distributed Logs (UUID v4, 1B events/day)",
            IDSystem.UUID_V4,
            current_items=100_000_000_000,
            growth_rate=1_000_000_000
        ),
    ]

    print("\n" + "=" * 70)
    print(" Production System Collision Analysis")
    print("=" * 70)

    for scenario in scenarios:
        risk = scenario.current_risk()
        days_left = scenario.days_until_risk()
        safety = scenario.safety_factor()

        print(f"\n{scenario.name}")
        print(f"  System: {scenario.system.description}")
        print(f"  Current items: {scenario.current_items:,}")
        print(f"  Growth: {scenario.growth_rate:,}/day")
        print(f"  Collision risk: {risk:.2e}")

        if risk > scenario.acceptable_risk:
            print(f"  ⚠️  RISK EXCEEDED - Immediate action needed!")
        elif days_left and days_left < 365:
            print(f"  ⏰ Time to threshold: {days_left:.0f} days")
        else:
            print(f"  ✅ Safe for years at current growth")

        print(f"  Safety factor: {safety:.1f}x before 50% collision")

def plot_collision_curves() -> None:
    """Visualize collision probabilities across ID systems."""
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    from collision_probability import collision_probability

    fig, ax = plt.subplots(figsize=(10, 6))

    # Define systems to compare
    systems = [
        (IDSystem.INT32, "32-bit", "red"),
        (IDSystem.INT64, "64-bit", "blue"),
        (IDSystem.UUID_V4, "UUID v4", "green"),
    ]

    # Generate log-spaced points for smooth curves
    for system, label, color in systems:
        space = system.space_size
        max_n = min(int(math.sqrt(space) * 100), 10 ** 15)
        n_values = np.logspace(1, np.log10(max_n), 200)

        # Calculate probabilities
        probs = [collision_probability(int(n), space) for n in n_values]

        ax.loglog(n_values, probs, color=color,
                  linewidth=2, label=label)

        # Mark 50% collision point
        n_50 = find_collision_threshold(space, 0.5)
        if n_50 <= max_n:
            ax.scatter([n_50], [0.5], color=color, s=100,
                       zorder=5, edgecolors='black')

    # Add risk thresholds
    ax.axhline(y=0.5, color='black', linestyle=':', alpha=0.5)
    ax.axhline(y=0.01, color='orange', linestyle=':', alpha=0.5)
    ax.axhline(y=1e-6, color='yellow', linestyle=':', alpha=0.5)

    # Danger zone
    ax.axhspan(0.01, 1.0, color='red', alpha=0.1)
    ax.text(100, 0.1, "DANGER ZONE", fontsize=12,
            fontweight='bold', color='darkred')

    ax.set_xlabel('Number of Items', fontsize=12)
    ax.set_ylabel('Collision Probability', fontsize=12)
    ax.set_title('Birthday Paradox in Production Systems', fontsize=14)
    ax.legend(loc='lower right')
    ax.grid(True, alpha=0.3, which="both")
    ax.set_xlim([10, 10 ** 15])
    ax.set_ylim([10 ** -18, 1])

    plt.tight_layout()
    plt.show()

def plot_time_to_collision() -> None:
    """Show how long systems last before first collision."""
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(figsize=(10, 6))

    # Generation rates (items per second)
    rates = np.logspace(0, 9, 100)  # 1 to 1 billion per second

    systems = [
        (IDSystem.INT32, "32-bit", "red"),
        (IDSystem.INT64, "64-bit", "blue"),
        (IDSystem.UUID_V4, "UUID v4", "green"),
    ]

    for system, label, color in systems:
        n_50 = find_collision_threshold(system.space_size, 0.5)
        years = n_50 / (rates * 365.25 * 24 * 3600)
        ax.loglog(rates, years, color=color, linewidth=2, label=label)

    # Add reference lines
    ax.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
    ax.text(1e9, 1.5, "1 year", fontsize=10)
    ax.axhline(y=100, color='gray', linestyle='--', alpha=0.5)
    ax.text(1e9, 150, "100 years", fontsize=10)

    # Add collision time annotations at 1 billion IDs/second
    # 32-bit: 77 microseconds
    ax.axhline(y=2.44e-9, color='red', linestyle=':', alpha=0.3)  # 77 microseconds in years
    ax.text(5e8, 3e-9, "77 μs", fontsize=9, color='red')

    # 64-bit: 1.4 hours
    ax.axhline(y=1.6e-4, color='blue', linestyle=':', alpha=0.3)  # 1.4 hours in years
    ax.text(5e8, 2e-4, "1.4 hours", fontsize=9, color='blue')

    # UUID v4: 86 years (already close to the 100 years line)
    ax.text(5e8, 70, "86 years", fontsize=9, color='green')

    ax.set_xlabel('Generation Rate (IDs per second)', fontsize=12)
    ax.set_ylabel('Time to 50% Collision (years)', fontsize=12)
    ax.set_title('How Long Until Your First Collision?', fontsize=14)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    """Run birthday paradox demonstrations and analysis."""

    # Classic birthday problem
    print("\n📅 Classic Birthday Problem:")
    n = 23
    prob = exact_collision_probability(n, 365)
    print(f"With {n} people: {prob:.1%} chance of shared birthday")

    # Monte Carlo validation
    print("\n🎲 Monte Carlo Validation:")
    simulated = collision_simulator(n, 365, trials=10000)
    print(f"Theoretical: {prob:.3f}, Simulated: {simulated:.3f}")

    # UUID analysis
    print("\n🔑 UUID v4 Analysis:")
    uuid_space = 2 ** 122
    for risk, desc in [(1e-6, "1-in-million"), (0.5, "50% risk")]:
        n_items = find_collision_threshold(uuid_space, risk)
        print(f"{desc}: {n_items:.2e} UUIDs")

    # Production systems
    analyze_production_systems()

    # Quick reference
    print("\n📊 Quick Reference - 50% Collision Points:")
    for name, bits in [("32-bit", 32), ("64-bit", 64), ("UUID v4", 122)]:
        n_50 = find_collision_threshold(2 ** bits, 0.5)
        print(f"  {name:10s}: {n_50:,.0f} items")

    plot_collision_curves()
    plot_time_to_collision()