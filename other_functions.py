def is_not_factor_of(
    *,
    number: int,
    factors: list[int],
) -> bool:
    """
    Checks if no number in `factors` is a factor of `number`.
    Args:
        number: Natural number to check.
        factors: List of natural numbers to check.
    Returns:
        True if no number in `factors` is a factor of `number`, False otherwise.
    """
    sorted_factors = sorted(factors)
    for factor in sorted_factors:
        if number % factor == 0 and number > factor:
            return False
        if number <= factor:
            return True
    return True


def is_not_factor_of_primes(
    *,
    primes: list[int],
    number: int,
    sort_primes: bool = False,
) -> bool:
    """
    Variation of `is_not_factor_of` function for more efficiency.
    Useful to determine if `number` is prime if the numbers of `primes` are primes and < `number`.
    Args:
        primes: List of prime numbers to check.
        number: Natural number to check.
        sort_primes: Whether to sort the list of primes. Default is False.
    Returns :
        True if no prime number in `primes` is a factor of `number`, False otherwise.
    """
    if sort_primes:
        primes = sorted(primes)
    # Only check primes up to sqrt(number) because if number is divisible by a prime greater than sqrt(number),
    # then it is divisible by a prime less than sqrt(number).
    square_root_of_number = int((number + 1) ** (1 / 2))
    for prime in primes[: square_root_of_number + 1]:
        if number % prime == 0:
            return False
    return True


def product_of_elements(elements: list[int]) -> int:
    """
    Returns the product of all elements of `elements` in a recursive way.
    Args:
        elements: List of natural numbers to multiply.
    Returns:
        Product of all elements of `elements`
    """
    if len(elements) == 1:
        return elements[0]
    last_element = elements[-1]
    other_elements = elements[:-1]
    return last_element * product_of_elements(other_elements)
