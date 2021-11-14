import math
import itertools
import operator


def is_prime(n):
    '''Check for a prime.'''

    if not isinstance(n, int):
        raise TypeError('Argument should be a positive integer.')

    if n < 2 or (n > 2 and n % 2 == 0):
        return False

    start = 3
    stop = int(math.sqrt(n)) + 1
    step = 2
    for i in range(start, stop, step):
        if n % i == 0:
            return False
    return True


def primes_under(n):
    '''Return a list of primes less than or equal to a given number.'''

    if not isinstance(n, int):
        raise TypeError('Argument should be a positive integer.')

    primes = []
    if n <= 1:
        return primes

    primes.append(2)
    for i in range(3, n + 1, 2):
        limit = int(math.sqrt(i)) + 1
        for j in primes:
            if j < limit:
                if i % j == 0:
                    break
            else:
                primes.append(i)
                break
        else:
            primes.append(i)

    return primes


def primes_between(a, b):
    '''Return a list of primes between 2 numbers, inclusive.'''

    for x in a, b:
        if not isinstance(x, int):
            raise TypeError(f'{x} is not an integer.')

    if a > b:
        return []

    before = primes_under(a - 1)
    between = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            continue
        limit = int(math.sqrt(i)) + 1
        for j in before:
            if j < limit:
                if i % j == 0:
                    break
            else:
                before.append(i)
                between.append(i)
                break
        else:
            before.append(i)
            between.append(i)

    return between


def prime_under(n):
    '''Return the greatest prime less than the given number.'''

    if n <= 2:
        return None

    while n > 2:
        n -= 1
        if is_prime(n):
            return n


def prime_over(n):
    '''Return the smallest prime greater than the given number.'''

    if n < 0:
        raise ValueError('Argument should be a positive integer.')

    while True:
        n += 1
        if is_prime(n):
            return n


def factors(n):
    '''Return a list of the factors of the given number, including 1 and
    itself.
    '''

    fs = []
    stop = n // 2 + 1
    for i in range(1, stop):
        if n % i == 0:
            fs.append(i)
    fs.append(n)

    return fs


def prime_factors(n):
    '''Return a list of the prime factors of the given number.'''

    return [factor for factor in factors(n) if is_prime(factor)]


def prime_factorise(n, show=False):
    '''Prime factorisation.

    If `show` is True, print an expression of the form:
    a^p * b^q * c^r
    where a, b, c, etc. are prime factors of n and p, q, r, etc. are
    their powers.

    Return a list of tuples of prime factor and power.
    '''
    result = []

    for prime in prime_factors(n):
        power = 0
        while n % prime == 0:
            power += 1
            n //= prime
        result.append((prime, power))

    if show:
        s = ' * '.join(f'{el[0]}^{el[1]}' for el in result)
        print(s)

    return result


def number_of_divisors(n):
    '''Number of divisors of the number, including 1 and itself.

    If prime factorisation of n = a^p * b^q * c^r, then number of
    divisors is (p+1)(q+1)(r+1).
    '''

    pf = prime_factorise(n)
    num_divisors = math.prod(power + 1 for _, power in pf)
    return num_divisors


def number_of_factor_pairs(n):
    '''Return the number of ways n can be resolved into 2 factors.

    Formula: If prime factorisation is a^p * b^q * c^r and n is not a
    perfect square, the required value is 1/2 * (p+1)(q+1)(r+1). If n is
    a perfect square, the required value is 1/2 * [(p+1)(q+1)(r+1) + 1].
    '''

    num_divisors = number_of_divisors(n)
    sqrt = math.sqrt(n)
    if sqrt == int(sqrt):
        return (num_divisors + 1) // 2
    return num_divisors // 2


def factor_pairs(n):
    '''Return a list of pairs of factors of n whose product gives n.'''

    fs = factors(n)
    pairs = []

    for pair in itertools.combinations(fs, 2):
        if operator.mul(*pair) == n:
            pairs.append(pair)

    return pairs


def number_of_mutually_prime_factor_pairs(n):
    '''Return the number of mutually prime factors of n.

    Formula: 2^(m - 1) where m is the number of prime factors.
    '''

    num_pf = len(prime_factors(n))
    return 2 ** (num_pf - 1)


def are_mutually_prime(a, b):
    '''Return True if the numbers a and b do not have a common factor
    apart from unity.
    '''

    fs_a = factors(a)
    fs_b = factors(b)

    common = set(fs_a).intersection(fs_b)
    if len(common) == 1:
        return True
    return False


def mutually_prime_factor_pairs(n):
    '''Return the factor pairs of n that do not have a common factor
    apart from unity.
    '''

    pairs = factor_pairs(n)
    mutually_prime_pairs = []

    for pair in pairs:
        if are_mutually_prime(*pair):
            mutually_prime_pairs.append(pair)

    return mutually_prime_pairs


def sum_of_divisors(n):
    '''Sum of divisors of n.

    Formula: If prime factorisation of n = a^p * b^q * c^r, then
    sum of divisors = (a^(p+1) - 1)/(p - 1) * (b^(q+1) - 1)/(q - 1)...
    '''

    pfs = prime_factorise(n)
    result = 1

    for prime, power in pfs:
        result *= (prime**(power + 1) - 1) // (prime - 1)

    return result


def highest_power(m: int, n: int):
    '''Highest power of a prime m in n!

    Formula: Sum of greatest integers contained in (n / m^i), where i
    is 1, 2, 3, etc.
    '''

    if not is_prime(m):
        raise TypeError('First argument should be a prime number.')

    cnt = 0
    i = 1
    while True:
        if n / m ** i < 1:
            break
        cnt += n // m ** i
        i += 1

    return cnt
