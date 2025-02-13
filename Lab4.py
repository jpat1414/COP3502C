def fibonacci(n):
    if n < 2:
        return n
    else:
        (a, b) = (0, 1)
        for i in range(n-1):
            a, b = b, a+b
        return a


def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        return True



def print_prime_factors(arg):
    n = arg
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors += [i]
            n //= i
        else :
            i += 1
    result = str(factors[0])
    for j in range(1, len(factors)):
        result += " * " + str(factors[j])

    return str(arg) + " = " + result
