while True:
    a,b,c,d = map(int, input().split())
    if (a+b+c+d) == 0:
        break
    ans = 360*3
    ans += ((a-b+40)%40)*9
    ans += ((c-b+40)%40)*9
    ans += ((c-d+40)%40)*9
    print(ans)

