""" Given Task 
    arr = [2,1,5,7,10]
    first maximum points obtain from cards but condition is that either k first element or k last element can be added also only k elemenet should added
    example k = 4 first four element or last four element can be added in between
    also total element to be added is 4 and having maximum sum is result
"""

""" Optimal solution 
    Use two pointer lsum and rsum to add left and right part of it
"""

arr = [6,2,3,4,7,2,1,7,1]
k = 4
lsum = 0
rsum = 0
l = 0
rindex = len(arr) - 1
maxsum = 0

for i in range(0 , k):
    lsum = lsum + arr[i]

for l in range(k-1, -1, -1):
    lsum = lsum - arr[l]
    rsum = rsum + arr[rindex]
    rindex -=1
    maxsum = max(maxsum, lsum + rsum)

print(maxsum)