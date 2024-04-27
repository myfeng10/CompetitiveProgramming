n,x0,y0=map(int,input().split())
myset =set()
# slope: coordinate
for _ in range(n):
    x,y = map(int,input().split())
    slope = (y-y0)/(x-x0) if x-x0!=0 else "inf"
    myset.add(slope)
print(len(myset))