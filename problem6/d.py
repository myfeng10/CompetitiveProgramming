n= int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def ford_fulkerson():
    pass

# default graph for min win
min_win={}
min_win[0]={1:a[0],2:a[1],3:a[2]} # initialize the edges to source

# forward edges
min_win[1] = {4:0,6:0}
min_win[2] = {4:0,5:0}
min_win[3] = {5:0,6:0}

# backward edges
min_win[4] = {1:n,2:n,7:b[0]}
min_win[5] = {2:n,3:n,7:b[1]}
min_win[6] = {1:n,3:n,7:b[2]}








print(a)
print(b)