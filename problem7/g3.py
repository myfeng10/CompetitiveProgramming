import io,os
import sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

#Sieve of Eratosthenes
n = 10000000
isPrime = [True for _ in range(n + 1)]

def sieve():
    for i in range(2, n + 1):
         if isPrime[i]:
            for j in range(2 * i, n + 1, i):
                isPrime[j] = False 

sieve()

t = 1
while t > 0:
    t -= 1
    n = int(input())

    a = [int(x) for x in input().split()]
    d1 = [-1 for _ in range(n)]
    d2 = [-1 for _ in range(n)]
    
    for i in range(n):
        #Find Smallest Prime Divisor of a[i]
        for SPD in range(min(2, a[i]), a[i] + 1):
            if a[i]%SPD==0:
                break

        p, q = SPD, a[i]

        while p!=1 and q%p==0:
            q //= p

        d1[i], d2[i] = p, q

        if d1[i] == 1 or d2[i] == 1:
            d1[i] = -1
            d2[i] = -1
            
    sys.stdout.write(" ".join(map(str, d1)) + "\n")
    sys.stdout.write(" ".join(map(str, d2)) + "\n")
        