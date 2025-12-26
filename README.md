# Prime Functions for Python

Some functions to play with prime numbers **for python**.

Some of them are similar (or equal) to functions from SymPy library.

Implemented functions:

- `inefficient_is_prime(n)`: Inefficient (and simplest) way to verify if a number is prime or not. Returns True if integer n is prime.
- `is_prime(n)`: More efficient way to verify if a number is prime or not. Returns True if integer n is prime.
- `all_previous_primes(n)`: Efficient way of making a list of primes <= n.
- `are_coprime(a, b)`: It verifies if two numbers doesn't have factors in common. Checkout the definition of coprimes for more info. Returns True if a and b are coprimes.
- `next_prime(n)`: Returns the next prime > n.
- `previous_prime(n)`: Returns the previous prime < n.
- `prime_range(a, b)`: Returns a list of prime numbers in the range [a, b[.
- `prime_pi(n)`: Returns the number of prime numbers <= n.
- `is_sheldon_prime(n)`: Returns True if number n is a sheldon prime. Checkout the definition of sheldon prime to more info.
- `nth_prime(nth)`: Returns nth prime number. In case nth < 1, returns None.

Also is featured the primality test (in this case, Solovay-Strassen primality test). It is a randomized probabilistic test, so it can verify if a number is prime. It is very efficient and it is implemented in the `primality_test` file.

Other functions:

- `is_not_factor_of(number, factors)`: Returns True if no number in `factors` is factor of `number`.
- `product_of_elements(elements)`: Returns the product of all elements of `elements` in a recursive way.
- `is_not_factor_of_primes(primes, number)`: Variation of `is_not_factor_of` function for more efficiency. Useful to determine if `number` is prime if the numbers of `primes` are sorted and are primes < `number`.
