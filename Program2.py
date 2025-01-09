def calculate_simplex_tax(income):
    """
    Calculates the Simplex Tax for a given annual income.

    Args:
        income (int): Annual income in dollars.

    Returns:
        int: Calculated tax rounded down to the nearest whole dollar.
    """
    tax = 0

    if income > 100000:
        tax += (income - 100000) * 0.3
        income = 100000

    if income > 50000:
        tax += (income - 50000) * 0.2
        income = 50000

    if income > 10000:
        tax += (income - 10000) * 0.1

    return int(tax)


if __name__ == "__main__":
    examples = [30000, 120000, 75000]
    for example in examples:
        print(f"Income: {example}, Tax: {calculate_simplex_tax(example)}")


def test_calculate_simplex_tax():
    """Test the calculate_simplex_tax function with various test cases."""
    assert calculate_simplex_tax(30000) == 2000
    assert calculate_simplex_tax(120000) == 19000
    assert calculate_simplex_tax(75000) == 9000
    assert calculate_simplex_tax(10000) == 0
    assert calculate_simplex_tax(50000) == 4000
    assert calculate_simplex_tax(0) == 0
    assert calculate_simplex_tax(150000) == 29000

    print("All tests passed!")


test_calculate_simplex_tax()
