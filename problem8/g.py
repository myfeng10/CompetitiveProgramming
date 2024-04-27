import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())                    # n is length of string, k is number of operation
    s = input()                                         # s is the correct spell
    t = input()                                         # t is the curse

    # for k in range(k+1):                                # k is the number of operation
    #     print("--> k",k)
    cnt = [0] * 26
    ok = True
    for i in range(n):                              # loop over every single character in the string
        print("i",i)
        if i >= k or i + k < n:                     # if i is >= k or i+k < n -> can swap this 
            cnt[ord(s[i]) - ord('a')] += 1          # +1 -> can swap this       
            cnt[ord(t[i]) - ord('a')] -= 1          # -1 -> can swap this
            print(s[i],t[i])
            print(cnt)
        else:
            ok &= s[i] == t[i]
            print("ok",ok)
    
    print("YES" if ok and cnt.count(0) == 26 else "NO")         # cnt.count(0) == 26: 

t = int(input())

for _ in range(t):
    solve()