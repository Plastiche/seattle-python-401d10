def fibonacci(n):
    """
    """
    number1 = 0
    number2 = 1
    count = 2

    if n == 0 or n == 1:
        return n

    while count < n + 1:
        nth = number1 + number2
        number1 = number2
        number2 = nth
        count += 1
    return nth


def recursive_fib(n):
    """
    """
    if n == 0 or n == 1:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)


def lucas(n):
    number1 = int(1)
    number2 = int(1)
    count = int(0)
    if n == 0:
        return 0
    while count < n:
        nth = number1 + number2
        number1 = number2
        number2 = nth
        count += 1
    return nth


if __name__ == "__main__":
    print(fibonacci(4))
