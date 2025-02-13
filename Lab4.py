def fibonacci(n):
    if n = 1:
        return n
    elif n = 0 
        return 0
    else:
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return a

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True




def print_prime_factors(arg):
    n = arg
    factors = ""
    i = 2
    first = True  

    while n > 1:
        if n % i == 0:
            if first:
                factors += str(i)
                first = False
            else:
                factors += " * " + str(i)
            n //= i
        else:
            i += 1

    print(str(arg) + " = " + factors)

