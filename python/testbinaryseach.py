
def binarySearchTree(arr, val, l, r):
    mid =  (l + r) // 2
    if arr[mid] == val:
        return mid
    elif val < arr[mid]:
        return  binarySearchTree(arr, val, l, mid)
    else:
        return binarySearchTree(arr, val, mid+1, r)
        

arr = [1,2,3,4,5,6,7]
arr.sort()
val = 4
n = len(arr)
output = binarySearchTree(arr, val, 0 ,n)
print(output)
