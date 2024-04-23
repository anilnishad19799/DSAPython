""" Given Task 
    arr = [1,0,1,0,1]
    first all binary substring having sum = k
    in above example let say [101, 1010, 0101,101] are substring having with sum=k
"""


""" Brute Force Approach """

arr = [1,0,1,0,1]
n = len(arr)
count = 0
k = 2
for i in range(n):
    for j in range(i, n):
        
        if arr[i] + arr[j] == k:
            count+=1
        
        if arr[i] + arr[j] > k:
            break

print(count)
        