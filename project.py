def remainder_without_mod(numerator, divisor):
    """
    1: (Task 0.5.2) Remainder
    >>> remainder_without_mod(28,7)
    0
    >>> remainder_without_mod(30,7)
    2
    """
    return numerator - ((numerator // divisor) * divisor)


def divisible_by_3(num):
    """
    2: Divisibility
    >>> divisible_by_3(9)
    True
    >>> divisible_y_3(7)
    False
    """
    return num % 3 == 0
