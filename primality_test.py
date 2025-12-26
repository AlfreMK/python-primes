import random


# The following code is extracted from the following link:
# https://github.com/IIC2283/DAA-2022-2/blob/main/codigo/alg_teoria_numeros.py
# all credits to the authors of the code.


def is_prime(number: int, iterations: int = 100) -> bool:
    """
    Checks if a number is prime or not using the Solovay-Strassen primality test.
    The probability of error of the test is less or equal to 2**(-iterations).
    Args:
        number: Natural number to check.
        iterations: Natural number to set the number of iterations.
    Returns:
        True if `number` is a prime number, False otherwise.
    """
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    elif is_power(number):
        return False
    neg = 0
    for i in range(1, iterations + 1):
        a = random.randint(2, number - 1)
        if gcd(a, number) > 1:
            return False
        else:
            b = exp_mod(a, (number - 1) // 2, number)
            if b == number - 1:
                neg = neg + 1
            elif b != 1:
                return False
    if neg > 0:
        return True
    else:
        return False


def is_power(number: int) -> bool:
    """
    Checks if a number is a power of another number.
    Args:
        number: Natural number to check if it is a power of another number.
    Returns:
        True if there is a natural number a and a natural number b such that number = (a**b),
        where a >= 2 and b >= 2, False otherwise.
    Example:
        is_power(8) -> True because 2**3 = 8
        is_power(27) -> True because 3**3 = 27
        is_power(16) -> True because 2**4 = 16
        is_power(15) -> False because there is no natural number a and b such that 15 = (a**b)
    """
    if number <= 3:
        return False
    else:
        k = 2
        lim = 4
        while lim <= number:
            if has_int_root(number, k):
                return True
            k = k + 1
            lim = lim * 2
        return False


def exp_mod(number: int, exponent: int, modulus: int) -> int:
    """
    Raises a number to the power of an exponent modulo a modulus.
    Args:
        a: Natural number to raise to the power of.
        b: Natural number to raise `a` to the power of.
        n: Natural number to modulo the result by.
    Returns:
        `a` raised to the power of `b` modulo `n`.
    """
    if exponent == 0:
        return 1
    elif exponent > 0:
        res = 1
        pot = number
        while exponent > 0:
            if exponent % 2 == 1:
                res = (pot * res) % modulus
            exponent = exponent // 2
            pot = (pot * pot) % modulus
        return res
    else:
        return exp_mod(modular_inverse(number, modulus), -exponent, modulus)


def gcd(a: int, b: int) -> int:
    """
    Args :
        a: int
        b: int - a > 0 o b > 0
    Returns :
        greatest common divisor between a & b
    """
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a


def has_int_root(number: int, exponent: int) -> bool:
    """
    Checks if a number has an integer root.
    Args:
        number: Natural number to check if it has an integer root.
        exponent: Natural number to raise `number` to the power of.
    Returns:
        bool - True if there is a natural number a such that n = (a**k),
        where a >= 2. In other case returns False.
    Example:
        has_int_root(8, 3) -> True because 2**3 = 8
        has_int_root(27, 3) -> True because 3**3 = 27
        has_int_root(16, 4) -> True because 2**4 = 16
        has_int_root(15, 4) -> False because there is no natural number a such that 15 = a**4
    """
    if number <= 3:
        return False
    else:
        a = 1
        while exp(a, exponent) < number:
            a = 2 * a
        return has_int_root_interval(
            number=number,
            exponent=exponent,
            interval_start=a // 2,
            interval_end=a,
        )


def has_int_root_interval(
    *,
    number: int,
    exponent: int,
    interval_start: int,
    interval_end: int,
) -> bool:
    """
    Checks if a number has an integer root in a given interval.
    Args :
        number: Natural number to check if it has an integer root.
        exponent: Natural number to raise `number` to the power of.
        interval_start: Natural number to start the interval.
        interval_end: Natural number to end the interval.
    Returns :
        True if there is a natural number a such that number = (a**exponent),
        where interval_start <= a <= interval_end. In other case returns False.
    """
    if number < 1 or exponent < 2 or interval_start < 0 or interval_end < 0:
        raise ValueError(
            "Invalid arguments: number must be greater than 0, "
            "exponent must be greater than 1, "
            "interval start must be greater than 0, "
            "interval end must be greater than 0"
        )
    if interval_start > interval_end:
        raise ValueError(
            "Invalid arguments: interval start must be less than interval end"
        )
    while interval_start <= interval_end:
        if interval_start == interval_end:
            return number == exp(interval_start, exponent)
        else:
            p = (interval_start + interval_end) // 2
            val = exp(p, exponent)
            if number == val:
                return True
            elif val < number:
                interval_start = p + 1
            else:
                interval_end = p - 1
    return False


def exp(number: int, exponent: int) -> int:
    """
    Raises a number to the power of an exponent.
    Args :
        number: Natural number to raise to the power of `exponent`.
        exponent: Natural number to raise `number` to the power of.
    Returns :
        `number` raised to the power of `exponent`.
    """
    if exponent == 0:
        return 1
    else:
        res = 1
        pot = number
        while exponent > 0:
            if exponent % 2 == 1:
                res = pot * res
            exponent = exponent // 2
            pot = pot * pot
        return res


def modular_inverse(number: int, modulus: int) -> int:
    """
    Args :
        number: Natural number to find the modular inverse.
        modulus: Natural number to find the modular inverse. It must be coprime with `number`.
    Returns :
        int - inverse of `number` in module `modulus`.
    """
    (_, s, _) = extended_euclidean_algorithm(number, modulus)
    return s % modulus


def extended_euclidean_algorithm(number1: int, number2: int) -> tuple[int, int, int]:
    """
    Finds the greatest common divisor of two numbers using the extended Euclidean algorithm.
    Args :
        number1: Natural number to find the greatest common divisor.
        number2: Natural number to find the greatest common divisor.
    Returns :
        Tuple containing the greatest common divisor `GCD(number1, number2)` between `number1` and `number2`,
        and integers `s` and `t` such that `GCD(number1, number2) = s*number1 + t*number2`.
        The tuple is in the form `(r, s, t)`, where `r` is the greatest common divisor, `s` is the coefficient of `number1`,
        and `t` is the coefficient of `number2`.
    """
    r_0 = number1
    s_0 = 1
    t_0 = 0
    r_1 = number2
    s_1 = 0
    t_1 = 1
    while r_1 > 0:
        r_2 = r_0 % r_1
        s_2 = s_0 - (r_0 // r_1) * s_1
        t_2 = t_0 - (r_0 // r_1) * t_1
        r_0 = r_1
        s_0 = s_1
        t_0 = t_1
        r_1 = r_2
        s_1 = s_2
        t_1 = t_2
    return r_0, s_0, t_0
