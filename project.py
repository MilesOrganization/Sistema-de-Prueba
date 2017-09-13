def remander_without_mod(numerator, divisor):
    """
    2: (Task 0.5.2) Remainder
    >>> remainder_without_mod(28,7)
    0
    >>> remainder_without_mod(30,7)
    2
    """
    return numerator - ((numerator // divisor) * divisor)