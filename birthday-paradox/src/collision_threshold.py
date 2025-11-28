# collision_threshold.py

import math
import random

def find_collision_threshold(
        total_possible_values: int,
        target_prob: float = 0.5
) -> int:
    """
    Find how many items you can generate before hitting a collision
    risk level.

    Example: With 365 possible birthdays, how many people before
    50% chance of a shared birthday? Answer: 23 people.
    """

    # If target is 0% or negative, you can't generate ANY items
    # (Even 1 item would exceed 0% risk)
    if target_prob <= 0:
        return 0

    # If target is 100% or more, you can generate more items than exist
    # (Collision is guaranteed anyway)
    if target_prob >= 1:
        return total_possible_values + 1

    # The formula is solving: "If I want 50% collision chance, and I have
    # 365 possible values, how many items do I need?"
    n_approx = math.sqrt(-2 * total_possible_values
                         * math.log(1 - target_prob))

    # Round up because we can't have 22.8 people - it's either 22 or 23
    # ceil(22.1) = 23, ceil(22.9) = 23, ceil(23.0) = 23
    return int(math.ceil(n_approx))

def collision_simulator(number_of_items: int,
                        total_possible_values: int,
                        trials: int = 10000) -> float:
    """Monte Carlo simulation to validate collision probability."""
    collisions = 0

    for _ in range(trials):
        seen = set()
        for _ in range(number_of_items):
            value = random.randint(0, total_possible_values - 1)
            if value in seen:
                collisions += 1
                break
            seen.add(value)

    return collisions / trials


if __name__ == '__main__':
    print("=" * 60)
    print("Testing Collision Threshold Calculator")
    print("=" * 60)

    # Test 1: Classic birthday problem
    print("\n1. Birthday Problem (365 days):")
    threshold = find_collision_threshold(365, 0.5)
    print(f"   50% collision at: {threshold} people")
    print(f"   Expected: 23 people")
    print(f"   ✓ PASS" if threshold == 23 else f"   ✗ FAIL")

    # Test 2: Verify with simulation
    print("\n2. Verify with Monte Carlo simulation:")
    simulated = collision_simulator(23, 365, 10000)
    print(f"   Simulated probability at 23 people: {simulated:.2%}")
    print(f"   Expected: ~50.7%")
    print(f"   ✓ PASS" if 0.48 < simulated < 0.53 else f"   ✗ FAIL")

    # Test 3: Different probability thresholds
    print("\n3. Different probability thresholds (365 days):")
    test_cases = [
        (0.01, 5),  # 1% risk
        (0.10, 14),  # 10% risk
        (0.50, 23),  # 50% risk
        (0.90, 41),  # 90% risk
        (0.99, 57),  # 99% risk
    ]

    for prob, expected in test_cases:
        result = find_collision_threshold(365, prob)
        status = "✓" if abs(result - expected) <= 1 else "✗"
        print(f"   {prob:3.0%} risk: {result:2d} people (expected ~{expected}) {status}")

    # Test 4: Edge cases
    print("\n4. Edge cases:")

    # Zero probability
    result = find_collision_threshold(365, 0.0)
    print(f"   0% probability: {result} (expected 0)")
    print(f"   ✓ PASS" if result == 0 else f"   ✗ FAIL")

    # 100% probability
    result = find_collision_threshold(365, 1.0)
    print(f"   100% probability: {result} (expected 366)")
    print(f"   ✓ PASS" if result == 366 else f"   ✗ FAIL")

    # Test 5: Small spaces
    print("\n5. Small value spaces:")
    result = find_collision_threshold(10, 0.5)
    print(f"   10 values, 50% risk: {result} items")
    simulated = collision_simulator(result, 10, 10000)
    print(f"   Simulated: {simulated:.2%}")
    print(f"   ✓ PASS" if 0.45 < simulated < 0.55 else f"   ✗ FAIL")

    # Test 6: Large spaces (like UUIDs)
    print("\n6. Large value spaces (UUID-like):")
    uuid_space = 2 ** 122
    threshold = find_collision_threshold(uuid_space, 1e-6)
    print(f"   UUID space (2^122)")
    print(f"   1-in-million risk at: {threshold:.2e} items")

    # Test 7: Verify threshold is correct
    print("\n7. Verify threshold accuracy:")
    space = 1000
    target = 0.5
    threshold = find_collision_threshold(space, target)

    # Test just below threshold
    below = collision_simulator(threshold - 1, space, 10000)
    # Test at threshold
    at = collision_simulator(threshold, space, 10000)

    print(f"   Space: {space}, Target: {target:.0%}")
    print(f"   Threshold: {threshold}")
    print(f"   Probability at {threshold - 1}: {below:.2%} (should be < {target:.0%})")
    print(f"   Probability at {threshold}: {at:.2%} (should be ≥ {target:.0%})")
    print(f"   ✓ PASS" if below < target <= at + 0.05 else f"   ✗ FAIL")

    print("\n" + "=" * 60)
    print("Testing complete!")
