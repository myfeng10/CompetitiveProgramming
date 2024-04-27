def Area(X,Y,n):
    area = 0.0
    j=n-1
    for i in range(n):
        area += (X[j]+X[i])*(Y[j]-Y[i])
        j=i
    return abs(area/2.0)