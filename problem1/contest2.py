
n = str(input())
new = ""
i = 0
distinct = 1
while i < len(n):
    n6= n[i:i+6]
    n10=n[i:i+10]
    n7=n[i:i+7]
    n9=n[i:i+9]
    n8=n[i:i+8]
    n4=n[i:i+4]
    n3=n[i:i+3]
    n5=n[i:i+5]
    if n10 == "zeroneight":
        new += "0n8"
        i += 10
    elif n9 == "twoneight":
        new += "2n8" 
        i += 9
    elif n6 == "zerone":
        new += "0ne" # < zer1
        i+=6
    elif n5 == "twone":
        new += "2ne" # length wise: same as tw1
        i+=5
        distinct +=1
    elif n7 == "oneight":
        new += "on8"
        i += 7
    elif n9 == "threeight":
        new += "3ight" # length wise: same as thre8
        i += 9
        distinct += 1
    elif n8 == "nineight":
        new += "nin8" 
        i += 8
    elif n8 == "fiveight":
        new += "fiv8"
        i += 8
    elif n3 == "one":
        new +="1"
        i += 3
    elif n3 == "two":
        new += "2"
        i+=3
    elif n5 == "three":
        new += "3"
        i+=5
    elif n4 == "four":
        new += "4"
        i+=4
    elif n4 == "five":
        new += "5"
        i+=4
    elif n3 == "six":
        new +="6"
        i+=3
    elif n5 == "seven":
        new += "7"
        i+=5
    elif n5 == "eight":
        new += "8"
        i+=5
    elif n4 == "nine":
        new += "9"
        i+=4
    elif n4 == "zero":
        new += "0"
        i+=4
    else:
        new += n[i]
        i+=1

print(len(new)) 
print(distinct%9302023)


# print()
print(new)