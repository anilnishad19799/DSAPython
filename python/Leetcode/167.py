""" Two sum problem for sorting array"""

numbers = [2,3,4]
target = 6

def getIndexOfSum(nums, target):
    # pass
    # l,r = 0,len(nums)-1
    # while(l<r):
    #     if nums[l] + nums[r] < target:
    #         l+=1
    #     elif nums[l] + nums[r] > target:
    #         r-=1
    #     else:
    #         return [l+1, r+1]
    
    # return []

    l,r = 0,1
    while(r<len(nums)):
        if nums[l] + nums[r] < target:
            r+=1
        elif nums[l] + nums[r] > target:
            l+=1
        else:
            return [l+1, r+1]
    
    return []


output = getIndexOfSum(numbers, target)
print(output)
