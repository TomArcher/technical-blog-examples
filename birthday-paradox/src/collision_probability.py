# collision_probability.py

import math

def collision_probability(number_of_items: int, total_possible_values: int) -> float:

    """
    Approximate collision probability for large spaces.
    P(collision) ≈ 1 - exp(-n²/2d)
    """
    if number_of_items > total_possible_values:
        return 1.0
    if number_of_items <= 1:
        return 0.0

    exponent = (-(number_of_items * (number_of_items - 1))
                / (2 * total_possible_values))
    return 1 - math.exp(exponent)

if __name__ == "__main__":
    input_data = [
        # Very small space, high collision probability
        (2, 2, 0.5),
        (3, 2, 1.0),

        # Small numbers, lower probability
        (2, 100, 0.1),
        (2, 100, 0.01),
        (2, 1000, 0.001),

        # Edge cases
        (0, 100, 0.0),
        (1, 100, 0.0),

        # Birthday paradox
        (23, 365, 0.5073)
    ]

    for number_of_items, total_possible_values, expected_collisions in input_data:
        result = collision_probability(number_of_items,
                                             total_possible_values)
        print(f"{number_of_items} items, {total_possible_values} total possible values, {result*100:.2f}% ≈ {expected_collisions*100:.2f}% expected collisions.")