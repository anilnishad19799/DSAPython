""" Given Task 
    arr = [3,3,3,1,2,1,1,2,3,3,4]
    find maximum consecutive ones haivng k zeros to fiiled at most
    for example at starting 3 consecutive one there but i can fill 2 consecutive zeros and if get third zeros then it should break and reurn maxlen = 5
    similarly for all the step is repeated to solve the problem
"""

""" brute force approach """
arr = [3,3,3,1,2,1,1,2,3,3,4]
k = 2
maxlen = 0

n = len(arr) - 1
for i in range(n):
    fruitset = set()
    for j in range(i, n):
        fruitset.add(arr[j])

        if len(fruitset) > k:
            break

        if len(fruitset) <= k:
            maxlen = max(maxlen, j-i+1)

print(maxlen)



""" Better approach using hashing technique"""

from collections import defaultdict

k = 2
l,r,maxlen,n =0,0,0,len(arr)-1
hash = defaultdict(int)

while (r < n):
    hash[arr[r]] +=1

    if len(hash) > k:
        while len(hash) > k:
            hash[arr[l]] -=1
            if hash[arr[l]] == 0:
                del hash[arr[l]]
            l+=1

    if len(hash) <= l:
        maxlen = max(maxlen, r-l+1)
    r+=1
print(maxlen)


""" Optimal approach is replace while condition to if"""
k = 2
l,r,maxlen,n =0,0,0,len(arr)-1
hash = defaultdict(int)

while (r < n):
    hash[arr[r]] +=1

    if len(hash) > k:
        if len(hash) > k:
            hash[arr[l]] -=1
            if hash[arr[l]] == 0:
                del hash[arr[l]]
            l+=1

    if len(hash) <= l:
        maxlen = max(maxlen, r-l+1)
    r+=1
print(maxlen)


