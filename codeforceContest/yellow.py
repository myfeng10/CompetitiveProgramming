while True:
    try:
        n1 = int(input())
        n3 = n1+1
        sol = []
        count = 0
        while n3<=n1*2:
            common = n1*n3
            d3 = common / n3
            d1 = common / n1
            d2 = d1-d3
            n2 = common / d2
            if int(n2)==n2:
                sol.append("1/"+str(n1)+" = "+"1/"+str(int(n2))+" + 1/"+str(n3))
                count+=1
            n3+=1 
        print(count)
        for e in sol:
            print(e)
    except EOFError:
        break