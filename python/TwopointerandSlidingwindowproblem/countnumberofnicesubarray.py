""" Given Task 
    arr = [1,1,2,1,1]
    first all odd integer having sum = k
    in above example let say [[1121], [1211]]]  are having with sum=k
"""

""" Optimal solution """



def binaryarraywithsum(arr, k):
    l,r,count = 0,0,0
    sum = 0
    n = len(arr)

    while r < n:
        sum = sum + (arr[r]%2)

        while sum > k:
            sum = sum - (arr[l] %2)
            l = l+1
        
        count += (r-l+1)
        r+=1

    return count

arr = [1,1,2,1,1]
k = 3
totalcount = binaryarraywithsum(arr, k) - binaryarraywithsum(arr, k-1)
print(totalcount)

