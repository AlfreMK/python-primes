"""
Prime functions for Python. Some of them are similar to functions from SymPy library.
These functions are not very efficient for big numbers. For big numbers, it is
recommended to use the functions from SymPy library or use the primality_test function
from primality_test.py file.
"""

from other_functions import product_of_elements, is_not_factor_of_primes


def inefficient_is_prime(number: int) -> bool:
    """
    Inefficient (and simplest) way to verify if a number is prime or not.
    Args :
        number: Natural number to check.
    Returns :
        True if `number` is prime, False otherwise.
    """
    for k in range(2, number):
        if number % k == 0:
            return False
    return True


def is_prime(number: int) -> bool:
    """
    More "efficient" way to verify if a number is prime or not. Not very efficient for big numbers.
    Args:
        number: Natural number to check.
    Returns:
        True if `number` is prime, False otherwise.
    """
    if (
        (number % 2 == 0 and number > 2)
        or (number % 3 == 0 and number > 3)
        or (number % 5 == 0 and number > 5)
        or number < 2
    ):
        return False
    k = 7
    while number ** (1 / 2) >= k:
        if number % k == 0 and number ** (1 / 2) >= k:
            return False
        k += 2
        if number % k == 0 and number ** (1 / 2) >= k:
            return False
        k += 2
        if number % k == 0 and number ** (1 / 2) >= k:
            return False
        k += 2
        if number % k == 0 and number ** (1 / 2) >= k:
            return False
        k += 4
    return True


def all_previous_primes(number: int) -> list[int]:
    """
    Returns a list of all primes <= `number`.
    Args:
        number: Natural number to get the previous primes.
    Returns:
        List of all primes <= `number`.
    """
    if number < 2:
        return []
    prime_numbers = [2]
    i = 3
    while number >= i:
        if is_not_factor_of_primes(primes=prime_numbers, number=i):
            prime_numbers.append(i)
        i += 2
    return prime_numbers


def are_coprime(number1: int, number2: int) -> bool:
    """
    It verifies if two numbers doesn't have factors in common.
    Args:
        number1: Natural number to check.
        number2: Natural number to check.
    Returns:
        True if `number1` and `number2` are coprime, False otherwise.
    """
    if (number1 % 2 == 0) and (number2 % 2 == 0):
        return False
    k = 3
    if number1 > number2:
        while number1 > k:
            if (number1 % k == 0) and (number2 % k == 0):
                return False
            k += 2
    else:
        while number2 > k:
            if (number1 % k == 0) and (number2 % k == 0):
                return False
            k += 2
    return True


def next_prime(number: int) -> int:
    """
    Returns the next prime > `number`.
    Args:
        number: Natural number to get the next prime.
    Returns:
        The next prime > `number`.
    """
    prime_numbers = all_previous_primes(number)
    if number % 2 == 0:
        number += 1
    while True:
        if is_not_factor_of_primes(primes=prime_numbers, number=number):
            return number
        number += 2


def previous_prime(number: int) -> int:
    """
    Returns the previous prime < `number`.
    Args:
        number: Natural number to get the previous prime.
    Returns:
        The previous prime < `number`.
    """
    prime_numbers = all_previous_primes(number - 1)
    return prime_numbers[len(prime_numbers) - 1]


def prime_range(number1: int, number2: int) -> list[int]:
    """
    Returns a list of prime numbers in the range [number1, number2[.
    Args:
        number1: Natural number to get the previous prime.
        number2: Natural number to get the next prime.
    Returns:
        List of prime numbers.
    """
    prime_numbers = all_previous_primes(number1)
    final_list = []
    if number1 <= 2:
        number1 = 2
        if number2 > 2:
            final_list.append(2)
    elif is_prime(number1):
        final_list.append(number1)
    while number1 < number2:
        if is_not_factor_of_primes(primes=prime_numbers, number=number1):
            prime_numbers.append(number1)
            final_list.append(number1)
        number1 += 1
    return final_list


def prime_pi(number: int) -> int:
    """
    Returns the number of prime numbers <= `number`.
    Args:
        number: Natural number to get the number of prime numbers <= `number`.
    Returns:
        The number of prime numbers <= `number`.
    """
    num = len(all_previous_primes(number))
    return num


def is_sheldon_prime(number: int) -> bool:
    """
    A sheldon prime is a prime number that satisfies the following conditions:
    - It is a prime number.
    - The product of its digits is a prime number.
    - The product of the digits of its inverse is a prime number.
    See https://en.wikipedia.org/wiki/73_(number)#Sheldon_prime.
    Args:
        number: Natural number to check.
    Returns:
        True if `number` is a sheldon prime, False otherwise.
    """
    inverse_number = int(str(number)[::-1])
    number_digits = [int(digit) for digit in str(number)]
    inverse_number_digits = number_digits[::-1]
    product_of_digits = product_of_elements(number_digits)
    inverse_product_of_digits = product_of_elements(inverse_number_digits)
    if not is_prime(number) or not is_prime(inverse_number):
        return False
    prime_numbers = (
        all_previous_primes(number)
        if number > inverse_number
        else all_previous_primes(inverse_number)
    )
    prime_pi_n = prime_numbers.index(number) + 1
    prime_pi_inv = prime_numbers.index(inverse_number) + 1
    if prime_pi_n != product_of_digits or inverse_product_of_digits != prime_pi_inv:
        return False
    return True


def nth_prime(nth: int) -> int:
    """
    Returns the nth prime number.
    Args:
        nth: Natural number to get the nth prime.
    Returns:
        The nth prime number.
    Raises:
        ValueError: If `nth` < 1.
    """
    prime_numbers = [2]
    i = 3
    num = 1
    if nth < 1:
        raise ValueError("nth must be greater than 0")
    elif nth == 1:
        return 2
    while nth > num:
        if is_not_factor_of_primes(primes=prime_numbers, number=i):
            prime_numbers.append(i)
            num += 1
        i += 2
    return i - 2
