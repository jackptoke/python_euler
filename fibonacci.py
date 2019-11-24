def fib(n):
    """Fibonaci series of less than n"""
    a, b = 0, 1
    result = []
    while a <  n:
        result.append(a)
        a, b = b, a + b
    return result

print(fib(2000))
print(fib(0))