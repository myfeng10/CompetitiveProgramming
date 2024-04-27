import math
final = []
for n in range(1,1000):
    count=0
    result=[]
    for i in range(1,n+1):
        if n%i==0:
            count+=1
            result.append(i)
    if count == 3:
        final.append(n)
        # print("YES")
    # print(result)
            
print(final)
result2 =[]
for i in final:
    result2.append(math.sqrt(i))
    

print(result2)