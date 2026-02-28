import math

def isPrime(a):
    for i in range (2 , int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

def primes_generator(n):
    for i in range(2 , n + 1):
        if isPrime(i):
            yield i
            
n = int(input())
for x in primes_generator(n):
    print(f"{x} ", end="")
    
            