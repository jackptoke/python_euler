def get_prime(nth):
    prime = [2, 3]
    n = prime[-1] + 2
    while len(prime) < nth:
        isPrime = True
        for x in prime:
            if n % x == 0:
                isPrime = False
                break 
        
        if isPrime:
            prime.append(n)
        n += 2
    return prime


def get_prime_less_than(target):
    prime = [2, 3]
    n = prime[-1] + 2
    while n < target:
        isPrime = True
        for x in prime:
            if n % x == 0:
                isPrime = False
                break 
        
        if isPrime:
            prime.append(n)
        n += 2
    return prime

# primes = get_prime(10001)
primes = get_prime_less_than(2000000)
print(f"The sume of all primes below 2 million is : {sum(primes)}")
print(f"The last prime is {primes[-1]}")



# print(f"The 10001st prime is: {primes[-1]}")