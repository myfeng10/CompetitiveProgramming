c = int(input())
report = 0
for x in range(c):
    operation = input().split(" ")
    #print(operation)
    if operation[0] == "donate":
        report += int(operation[1])
    else:
        print(report)