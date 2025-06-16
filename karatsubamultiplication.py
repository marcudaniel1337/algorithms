def karatsuba(x, y):
    """
    Multiply two integers x and y using the Karatsuba algorithm.

    Karatsuba multiplication reduces the multiplication of two n-digit numbers
    to at most three multiplications of n/2-digit numbers,
    which is faster than the traditional grade-school method for large numbers.

    Args:
        x (int): First number to multiply.
        y (int): Second number to multiply.

    Returns:
        int: The product of x and y.
    """

    # Base case for recursion:
    # If x or y is small enough, just multiply directly
    if x < 10 or y < 10:
        return x * y

    # Calculate the number of digits of the largest input number
    n = max(len(str(x)), len(str(y)))
    half = n // 2  # Split position

    # Split x into two halves: high (left) and low (right)
    high_x = x // 10**half
    low_x = x % 10**half

    # Split y into two halves: high (left) and low (right)
    high_y = y // 10**half
    low_y = y % 10**half

    # Recursively compute three products:
    # 1. z2 = high_x * high_y
    z2 = karatsuba(high_x, high_y)

    # 2. z0 = low_x * low_y
    z0 = karatsuba(low_x, low_y)

    # 3. z1 = (high_x + low_x) * (high_y + low_y) - z2 - z0
    z1 = karatsuba(high_x + low_x, high_y + low_y) - z2 - z0

    # Combine the three results to get the final product:
    # (z2 * 10^(2*half)) + (z1 * 10^half) + z0
    return (z2 * 10**(2 * half)) + (z1 * 10**half) + z0


if __name__ == "__main__":
    # Test with some large numbers
    num1 = 12345678901234567890
    num2 = 98765432109876543210

    print(f"Multiplying {num1} * {num2} using Karatsuba algorithm:\n")
    result = karatsuba(num1, num2)
    print(result)

    # Double check against Python's built-in multiplication
    assert result == num1 * num2, "Karatsuba result doesn't match built-in multiplication!"
    print("\nSuccess! The result matches Python's built-in multiplication.")
