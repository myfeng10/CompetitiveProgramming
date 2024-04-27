dic ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#n = "LVIII"
n = "III"
n = list(n)
for i in range(len(n)):
    n[i] = dic[n[i]]  
maximum = max(n)  
result = 0
i=0
while i < (len(n)-1):
    if n[i]>=n[i+1]:
        result += n[i]
        i+=1
    elif n[i]<n[i+1]:
        result += n[i+1]-n[i]
        i+=2
if i == len(n)-1:
    result += n[i]
print(result)

