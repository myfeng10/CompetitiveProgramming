import io,os
import sys
import math

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

#Sieve of Eratosthenes
n = 10000000
num = [0 for _ in range(n + 1)]                     # num[i]: smallest prime divisor of i

def sieve():
    for i in range(2, n + 1):
        if num[i]==0:                               # if i is a prime
            for j in range(2 * i, n + 1, i):        # mark all multiples of i as not prime
                if num[j] == 0:                     # if j has not been assigned with its smallest prime divisor
                    num[j] = i                      # mark i as j's smallest prime divisor, being marked means that j is not a prime
sieve()
t = 1
while t > 0:
    t -= 1
    n = int(input())

    a = [int(x) for x in input().split()]
    d1 = [-1 for _ in range(n)]
    d2 = [-1 for _ in range(n)]
    
    for i in range(n):
        if num[a[i]]==0:
            d1[i],d2[i]=-1,-1
            continue
        x=a[i]                                          # eg. a[i]=12, num[12]=2
        count = 0                                       # count the number of times num[i] divides a[i]
        while(True):                                    # find the smallest prime divisor of a[i]   
            if x%num[a[i]]==0:                          # 12/2 = 6, 6/2=3 count=2 -> this means that 12 is divisible by 2**2 = 4
                count=1
                x//=num[a[i]]
            else:
                break

        if x==1:
            d1[i],d2[i]=-1,-1
        else:
            d1[i]=int(math.pow(num[a[i]],count))        # d1 = 4 d2 = 3 when a[i]=12
            d2[i] = x

    sys.stdout.write(" ".join(map(str, d1)) + "\n")
    sys.stdout.write(" ".join(map(str, d2)) + "\n")
        