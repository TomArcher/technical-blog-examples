# exact_collision_probability.py

def exact_collision_probability(number_of_items: int,
                                total_possible_values: int) -> float:
    """
    Calculate exact probability of at least one collision.
    P(collision) = 1 - П(1 - i/d) for i from 0 to n-1
    Accurate for small n, may lose precision for large n.
    """
    if number_of_items > total_possible_values:
        return 1.0
    if number_of_items <= 1:
        return 0.0
    prob_no_collision = 1.0
    for i in range(number_of_items):
        prob_no_collision *= ((total_possible_values - i)
                           / total_possible_values)
        # Early exit for numerical stability
        if prob_no_collision < 1e-15:
            return 1.0
    return 1 - prob_no_collision