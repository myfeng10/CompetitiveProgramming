n = int(input())

for i in range(n):
    
    m = int(input())
    snow = [int(input()) for x in range(m)]
    #snow = [0,0,0,0,0]
    i = 0
    j = 0
    dict = {} # store the current encountered snowflakes
    track = [] # store all possible counts
    while j < len(snow) and i < len(snow):
        if snow[j] in dict:
            
            track.append(len(dict))
            #print(snow[j], "seen, resetting","track",track)
            i = dict[snow[j]]+1
            j = i
            dict = {} # reset the dictionary
        else:
           
            # if j is not in dic -> store j's location
            dict[snow[j]] = j
            #print(snow[j], "not seen, adding to dict,",dict)
            # move to next snowflake
            j+=1
    track.append(len(dict))
    #print("Tract,",track)
            
    print(max(track))
