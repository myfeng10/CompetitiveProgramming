def sieve_of_eratosthenes():
    n=10**6
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1): 
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

n = int(input())
b = list(map(int, input().split()))

prime = sieve_of_eratosthenes()
for i in b:
    if prime[int(i**0.5)] and i**0.5 == int(i**0.5):
        print("YES")
    else:
        print("NO")
