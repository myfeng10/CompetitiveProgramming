n = str(input())
special_count = 0
if "twone" in n:
    special_count += n.count("twone") 
    n = n.replace("twone", "2ne")
if "threeight" in n or "eighthree" in n:
    special_count += n.count("threeight")
    n = n.replace("threeight", "3ight")
if "zero" in n:
    n = n.replace("zero", "0")
if "eight" in n:
    n = n.replace("eight", "8")
if "seven" in n:
    n = n.replace("seven", "7") 
if "nine" in n:
    n = n.replace("nine", "9")   
if "six" in n:
    n = n.replace("six", "6")
if "five" in n:
    n = n.replace("five", "5")
if "four" in n:
    n = n.replace("four", "4")
if "three" in n:
    n = n.replace("three", "3")
if "two" in n:
    n = n.replace("two", "2")
if "one" in n:
    n = n.replace("one", "1")
print(len(n))
distinct = 2**special_count
print(distinct%9302023)


print("special",special_count)
print("distinct",distinct)
print(n)
# print(distinct)

