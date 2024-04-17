""" Given Task 
    arr = [2,1,5,7,10]
    first longest subsequence length which sum < k
    where k is 15
"""

""" Brute Force approach 
    Time complexity Big 0(N^2)
    """
arr = [2,1,5,1,1, 1]
k = 14
n = len(arr) - 1
sum = 0
maxlen = 0
for i in range(n):
    for j in range(n):
        sum += arr[j]
        if sum <= k:
            maxlen = max(maxlen, j-i+1)
        else:
            break

print(maxlen)


""" Better approach 
    Time complexity Big 0(2N)
"""
sum = 0
maxlen = 0
n = len(arr) - 1
l, r = 0, 0
while (r < n):
    sum = sum + arr[r]

    while sum > k:
        l = l+1
        sum = sum - arr[l]
    
    if sum <=k:
        maxlen = max(maxlen, r-l+1)

    r+=1

print(maxlen)

""" Optimnal solution it work only if we want to find length if we want substring value then it is not work upper logic work
    Time complexity Big 0(N)
"""
sum = 0
maxlen = 0
n = len(arr) - 1
l, r = 0, 0
while (r < n):
    sum = sum + arr[r]

    if sum > k:
        l = l+1
        sum = sum - arr[l]
    
    if sum <=k:
        maxlen = max(maxlen, r-l+1)

    r+=1

print(maxlen)
