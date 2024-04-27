a = ['flow','flower','flight']
prefix  = a[0]
for i in range(1,len(a)):
    while a[i].find(prefix) != 0:
        prefix = prefix[:-1]

print(prefix)