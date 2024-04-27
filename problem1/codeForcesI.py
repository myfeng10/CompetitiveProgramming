n = int(input())
all_cols = ["a","b","c","d","e","f","g","h"]
all_rows = [1,2,3,4,5,6,7,8]
for i in range(n):
    location = input()
    row = int(location[1])
    col = location[0]
    
    for c in range(len(all_cols)):
        if col != all_cols[c]:
            print(all_cols[c]+str(row))
    for r in range(len(all_rows)):
        if row != all_rows[r]:
            print(col+str(all_rows[r]))