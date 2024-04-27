from sys import stdout

primes  = [x for x in range(2,100) if 0 not in [x%i for i in range(2,x)]]
small = [x for x in primes if x<10]
square = [x**2 for x in primes if x**2 < 100]

for s in square:
    print(s)

