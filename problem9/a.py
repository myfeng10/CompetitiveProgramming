import math

ax,ay,bx,by,cx,cy = map(int, input().split())

dis_ab=(bx - ax) ** 2 + (by - ay) ** 2
dis_bc=(cx - bx) ** 2 + (cy - by) ** 2

if dis_ab==dis_bc and (by-ay)*(cx-bx)!=(cy-by)*(bx-ax):
    print("Yes")
else:
    print("No")
