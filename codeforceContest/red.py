first = True
total = int(input())
current=0
for _ in range(total):
    n = int(input())
    if first == True:
        current = n
        first = False
    else:
        if n%current==0:
            print(n)
            first = True
        
  