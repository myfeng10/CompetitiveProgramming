import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def dist(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

p = [Point() for _ in range(105)]
d = [0] * 105

tc = 0
n = int(input())
for _ in range(n):
    k, t = map(int, input().split())
    for i in range(k):
        p[i].x, p[i].y = map(float, input().split())

    ave = 0
    for i in range(1, k):
        d[i] = dist(p[i - 1], p[i] )
        ave += d[i]
    ave /= (t-1)

    acu = 0
    print("Road #{}:".format(tc + 1))
    print("{:.2f} {:.2f}".format(p[0].x, p[0].y))
    for i in range(1, k):
        acu += d[i]
        while acu > ave - 1e-4:
            acu -= ave
            angle = math.atan2(p[i].y - p[i - 1].y, p[i].x - p[i - 1].x)
            x = p[i].x - acu * math.cos(angle)
            y = p[i].y - acu * math.sin(angle)
            print("{:.2f} {:.2f}".format(x, y))
    print()
    tc += 1
