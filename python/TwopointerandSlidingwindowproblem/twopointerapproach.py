""" Based on two pointer approach ther are maily three-four approach used in two pointer and slidin window appraoch"""

""" Pattern as Follow
    1. constant windows
    2. Longest substring/ subarray
    3. No of subarray where coondition
    4. shortest/minimum windows
"""

"1 Constant Pattern"
""" Problem statement

    arr = [2,1,5,7,10] , given k = 4
    task = find minimum value by picking k consecutive element
"""


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


""" Lonest substring where condition

    largest subarray with sum <=k
"""

""" At first try brute force approach"""
sumk = 15
maxlen = 0

def findlongestsequenceforsumK(arr, k, maxlen):
    for i in range(len(arr)):
        sum = 0
        temp = 1
        for j in range(i, len(arr)):
            sum  = sum + arr[j]
            temp+=1
            if sum < sumk:
                if temp > maxlen:
                    maxlen = temp
            else:
                break
    return maxlen

maxlenval = findlongestsequenceforsumK(arr, sumk, maxlen)
print(maxlenval)


""" Now apply better approach using two pointer and sliding windows approach """

def betterlongestsubsequenceapproachsumK(arr, k, maxlen):
    l = 0
    r = 0
    sum = 0
    n = len(arr) - 1
    temp = 0
    while r<n:
        temp +=1
        sum = sum + arr[r]
        while sum > k:
            temp = 0
            sum = sum - arr[l]
            l+=1   # Here shrinking

        if temp > maxlen:
            maxlen = temp

        r+=1  #here expansion

    return maxlen

sumk = 15
maxlen = 0
maxlenval = betterlongestsubsequenceapproachsumK(arr, sumk, maxlen)
print(maxlenval)

""" The above is better approach with time compelxity is Big O(N+N)"""
""" But i have to increase it optimal solution by using if condition inplace of while condition I get Big 0(N) which is an optimal solution"""
""" But when i have to find subarray sequence then this optimal not work here """