def remander_without_mod(numerator, divisor):
    """
    2: (Task 0.5.2) Remainder
    >>> remainder_without_mod(28,7)
    0
    >>> remainder_without_mod(30,7)
    2
    """
    return numerator - ((numerator // divisor) * divisor)


def divisble_by_3(num):
    """
    3: (Task 0.5.3) Divisibility
    >>> divisible_by_3(9)
    True
    >>> divisibre_by_3(7)
    False
    """
    return "True" if num % 3 == 0 else "False"