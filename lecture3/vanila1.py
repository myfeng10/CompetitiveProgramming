def find_x(n, nums):
    for i in range(0,n):
        y = 0
        for j in range(0,n):
            if i != j:
                y ^= nums[j]
        if y == nums[i]:
            return y
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))  # n integers
    print(find_x(n, nums), end=" ")

def find_x(n, nums):
    for i in range(0,n):
        y = 0
        for j in range(0,n):
            if i != j:
                y ^= nums[j]
        if y == nums[i]:
            return y



t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))  # n integers
    print(find_x(n, nums), end=" ")