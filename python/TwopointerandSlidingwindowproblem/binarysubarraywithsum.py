""" Given Task 
    arr = [1,0,1,0,1]
    first all binary substring having sum = k
    in above example let say [101, 1010, 0101,101] are substring having with sum=k
"""



""" Optimal solution """

def binaryarraywithsum(arr, k):
    l,r,count = 0,0,0
    sum = 0
    n = len(arr)

    while r < n:
        sum = sum + arr[r]

        while sum > k:
            sum = sum - arr[l]
            l = l+1
        
        count += (r-l+1)
        r+=1

    return count

arr = [1,0,1,0,1]
k = 2
totalcount = binaryarraywithsum(arr, k) - binaryarraywithsum(arr, k-1)
print(totalcount)

