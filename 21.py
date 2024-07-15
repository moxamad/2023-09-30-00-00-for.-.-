numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_PrimeS = []
for i in numbers:
    is_prime = True
    if i <= 1:
        is_prime = False
    else:
        for a in range(2, int(i ** 0.5) + 1):
            if i % a == 0:
                is_prime = False
                break
    if is_prime:
        Primes.append(i)
    else:
        Not_PrimeS.append(i)

print("Primes:", Primes)
print("Not Primes:", Not_PrimeS)