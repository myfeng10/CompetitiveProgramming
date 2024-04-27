import sys
# Python3 Code Addition 
input=sys.stdin.readline
# limit for array size 
N = 200001; 

# Max size of tree 
tree = [0] * (4*N); 

# function to build the tree 
def build(arr) : 

    # insert leaf nodes in tree 
    for i in range(n) : 
        tree[n + i] = arr[i]; 
    
    # build the tree by calculating parents 
    for i in range(n - 1, 0, -1) : 
        tree[i] = tree[i << 1]+tree[i << 1 | 1]

# function to update a tree node 
def updateTreeNode(p, value) : 
    
    # set value at position p 
    tree[p + n] = value; 
    p = p + n; 

    i=p;
    # move upward and update parents     
    while i > 1 :
        tree[i >> 1] = tree[i]+ tree[i ^ 1]
        i >>= 1

# function to get sum on interval [l, r) 
def query(l, r) : 
    res = 0; 
    # loop to find the sum in the range 
    l += n; 
    r += n; 
    
    while l < r : 
    
        if (l & 1) : 

            res += tree[l]; 
            l += 1
    
        if (r & 1) : 
            r -= 1; 
            res +=tree[r]; 
            
        l >>= 1; 
        r >>= 1
    
    return res; 

n,m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
build(a)
for i in range(m):
    a,b=[int(x) for x in input().split()]
    print(query(a-1,b))