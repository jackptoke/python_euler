def is_prime(n):
    a = 2
    while a < n:
        if n % a == 0:
            return False
        a += 1
    return True


n = 2
target = 600851475143
max = 0
total = 1
while total < target :
    if target % n == 0:
        if is_prime(n):
            max = n
            print(max)
        total *= n
    n += 1

print(f"Max prime: {max} Largest n: {n}")