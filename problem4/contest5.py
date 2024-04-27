n = input() 
dp = [-1]*(len(n)+1)
dp[0]=0
count = [0]*(len(n)+1)
count[0]=1
outcome = {i:[] for i in range(len(n)+1)}
outcome[0].append("")
dict = {3:["one","two","six"],4:["four","five","nine","zero"],5:["three","seven","eight"]}
dict_numbers = { "zero": 0, "one": 1, "two": 2, "three": 3,"four": 4,"five": 5,"six": 6,"seven": 7,"eight": 8,"nine": 9}
# i loops through the string n
for i in range(len(n)):
    len3 = n[i-2:i+1]
    len4 = n[i-3:i+1]
    len5 = n[i-4:i+1]
    if i<2:
        dp[i+1]=dp[i]+1
        count[i+1] = count[i]
        outcome[i+1].append(outcome[i][0]+n[i])
    if i==2:
        if len3 in dict[3]:
            dp[i+1]=1

            outcome[i+1].append(outcome[i-2][0]+str(dict_numbers[len3]))
        else:
            dp[i+1] = dp[i]+1
            outcome[i+1].append(outcome[i][0] + n[i])
        count[i+1] = count[i]
        
    if i==3:
        if len4 in dict[4]:
            dp[i+1] = 1
            outcome[i+1].append(outcome[i-3][0]+str(dict_numbers[len4]))
        else:
            dp[i+1] = dp[i]+1 
            outcome[i+1].append(outcome[i][0]+n[i])
        count[i+1] = count[i]

    if i > 3:
        if len3 in dict[3]:
            dp[i+1] = min(dp[i-2]+1,dp[i]+1)

            if dp[i-2] == dp[i]: # count
                count[i+1]=(count[i-2] + count[i])
                for ele in outcome[i-2]:
                    outcome[i+1].append(ele + str(dict_numbers[len3]) )
                for ele in outcome[i]:
                    outcome[i+1].append(ele+n[i])
                
            elif dp[i+1] != dp[i]+1: # most recent symbol
                count[i+1] = count[i-2]
                for ele in outcome[i-2]:
                    outcome[i+1].append(ele + str(dict_numbers[len3]) )
            else:
                count[i+1] = count[i]
                for ele in outcome[i]:
                    outcome[i+1].append(ele + n[i])

        elif len4 in dict[4]:
            dp[i+1] = min(dp[i-3]+1,dp[i]+1)

            if dp[i+1] != dp[i]+1:
                count[i+1] = count[i-3]
                for ele in outcome[i-3]:
                    outcome[i+1].append(ele + str(dict_numbers[len4]) )
                outcome[i+1].append(outcome[i][0]+n[i])
            else:
                count[i+1] = count[i]
                for ele in outcome[i]:
                    outcome[i+1].append(ele + n[i] )
        elif len5 in dict[5]:
            dp[i+1] = min(dp[i-4]+1,dp[i]+1)

            if dp[i-4]==dp[i]: # repetitive
                count[i+1] = count[i-4]+count[i]
                for ele in outcome[i-4]:
                    outcome[i+1].append(ele + str(dict_numbers[len5]) )
                for ele in outcome[i]:
                    outcome[i+1].append(ele+n[i])
            elif dp[i+1] != dp[i]+1: # becomes a symbol
                count[i+1] = count[i-4]
                for ele in outcome[i-4]:
                    outcome[i+1].append(ele + str(dict_numbers[len5]))
            else:
                count[i+1] = count[i]
                for ele in outcome[i]:
                    outcome[i+1].append(ele + n[i] )

        else:
            dp[i+1] = dp[i]+1
            count[i+1] =count[i]
            for ele in outcome[i]:
                    outcome[i+1].append(ele + n[i] )
            
print(dp[-1])
print(count[-1]%9302023)

print()
print("count",count)
print("dp",dp)
print("str",outcome)