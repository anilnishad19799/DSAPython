""" Given Task 
    arr = [1,1,1,0,0,0,1,1,1,1,0]
    find maximum consecutive ones haivng k zeros to fiiled at most
    for example at starting 3 consecutive one there but i can fill 2 consecutive zeros and if get third zeros then it should break and reurn maxlen = 5
    similarly for all the step is repeated to solve the problem
"""

"""given array and k value"""

""" Here applying brute force approach having time complexity Big O(N^2) """
arr = [1,1,1,0,0,0,1,1,1,1,1,0]
k = 2
maxlen = 0

n = len(arr) - 1
for i in range(0, n):
    zeros = 0
    for j in range(i, n):
        if arr[j] == 0:
            zeros +=1
        
        if zeros <= k:
            maxlen = max(maxlen, j-i+1)
        else:
            break

print(maxlen)


""" Better approach having time complexity of Big O(2N)"""
l,r,maxlen,zeros = 0,0,0,0
n = len(arr) - 1

while(r<n):
    if arr[r] == 0:
        zeros +=1

    while zeros > k:
        if arr[l] == 0:
            zeros -=1
        l+=1

    if zeros <= k:
        maxlen = max(maxlen, r-l+1)
    
    r+=1


print(maxlen)

""" Optimal solutions having time complexity Big O(N)"""

l,r,maxlen,zeros = 0,0,0,0
n = len(arr) - 1

while(r<n):
    if arr[r] == 0:
        zeros +=1

    if zeros > k:
        if arr[l] == 0:
            zeros -=1
        l+=1

    if zeros <= k:
        maxlen = max(maxlen, r-l+1)
    
    r+=1


print(maxlen)
