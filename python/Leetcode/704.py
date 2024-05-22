def binarysearch(nums, target):
    l = 0
    r = len(nums)

    while l!=r:
        print(l,r)
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid+1
        elif target < nums[mid]:
            r = mid
        else:
            l = mid+1
    
    return -1

# nums = [-1,0,3,5,9,12] 
# target = 9

nums = [-1,0,3,5,9,12]
target = 2

output = binarysearch(nums, target)
print(output)