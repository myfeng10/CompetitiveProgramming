n = int(input())
def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

for _ in range(n):
    px, py = map(int, input().split())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())

    d1 = max(dist(0,0,ax,ay), dist(ax,ay,px,py))
    d2 = max (dist(0,0,bx,by), dist(bx,by,px,py))
    com = max(max(min(dist(px, py, ax, ay), dist(px, py, bx, by)), min(dist(bx, by, 0, 0), dist(ax, ay, 0, 0))), dist(ax,ay, bx, by)/2)
    fin = min(d1, d2, com)
    print("{:.9f}".format(fin))