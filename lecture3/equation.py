n = int(input())
for _ in range(n):
    A,B,C = map(int,input().split())
    solution = []
    for x in range(-22,23):
        for y in range(-100,101):
            if y!= 0 and x!=0:
                z1 = A-x-y
                z3 = C-x**2-y**2
                z2 = B/(x*y)
                if int(z2)==z2 and z1 == int(z2) == z3:
                    #z2 is an integer
                    solution.append([x,y,z1])
    if len(solution) == 0:
        print("No solution.")
    else:
        print(solution)
        solution1 = sorted(solution)
        print(solution1[0][0],solution1[0][1],solution1[0][2])
    
    