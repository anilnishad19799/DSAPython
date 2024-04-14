""" Here in this program i am going to use two pointer approach which is used to solve many problem
    find k consecutive sum max value from array
"""

""" Problem statement
    here given k = 4 find 4 consecutive array value which has maximum sum
"""
""" This is simple approach uses iterative war"""
k = 4
def findmaxKconsecutive(arr, k):
    sum = 0
    maxsum = 0
    for i in range(0, len(arr) - k + 1):
        j = i+1
        k = j+1
        l = k+1
        sum = arr[i] + arr[j] + arr[k] + arr[l]
        if sum > maxsum:
            maxsum = sum

    return maxsum


arr = [2,4,9,8,6,10,12]
maxsumval = findmaxKconsecutive(arr, k)
print(maxsumval)

""" Using two pointer and sliding windows approach"""
def findmaxsumconsecutivetwopointer(arr, k):
    sum = 0
    maxsum = 0

    l = 0
    r = k-1

    for i in range(0, k):
        sum = sum + arr[i]

    n = len(arr) - 1
    
    while( r<n):
        sum = sum - arr[l]
        l+=1
        r+=1
        sum = sum + arr[r]

        if sum > maxsum:
            maxsum = sum

    return maxsum

arr = [2,4,9,8,6,10,12]
maxsumval = findmaxsumconsecutivetwopointer(arr, k)
print(maxsumval)