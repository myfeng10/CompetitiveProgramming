n = "zeroneighton" # 0n8on
n ="twoneightone" #  2n8on
n = "zeronenn" # 0nenn
n = "twonenn" # 2nenn
n = "threeight808" # 3ight808 
n = "**nineight***" # **nin8***
n = "*one*two*three*four*five*six*seven*eight*nine*zero*"  
n="xxxx"
# 3 letters
n = str(input())
new = ""
i = 0
distinct = 1
while i < len(n):
    if n[i:i+10] == "zeroneight":
        new += "0n8"
        i += 10
    elif n[i:i+9] == "twoneight":
        new += "2n8" 
        i += 9
    elif n[i:i+6] == "zerone":
        new += "0ne" # < zer1
        i+=6
    elif n[i:i+5] == "twone":
        new += "2ne" # length wise: same as tw1
        i+=5
        distinct +=1
    elif n[i:i+7] == "oneight":
        new += "on8"
        i += 7
    elif n[i:i+9] == "threeight":
        new += "3ight" # length wise: same as thre8
        i += 9
        distinct += 1
    elif n[i:i+8] == "nineight":
        new += "nin8" 
        i += 8
    elif n[i:i+8] == "fiveight":
        new += "fiv8"
        i += 8
    elif n[i:i+3] == "one":
        new +="1"
        i += 3
    elif n[i:i+3] == "two":
        new += "2"
        i+=3
    elif n[i:i+5] == "three":
        new += "3"
        i+=5
    elif n[i:i+4] == "four":
        new += "4"
        i+=4
    elif n[i:i+4] == "five":
        new += "5"
        i+=4
    elif n[i:i+3] == "six":
        new +="6"
        i+=3
    elif n[i:i+5] == "seven":
        new += "7"
        i+=5
    elif n[i:i+5] == "eight":
        new += "8"
        i+=5
    elif n[i:i+4] == "nine":
        new += "9"
        i+=4
    elif n[i:i+4] == "zero":
        new += "0"
        i+=4
    else:
        new += n[i]
        i+=1

print(len(new)) 
print(distinct%9302023)


# print()
print(new)