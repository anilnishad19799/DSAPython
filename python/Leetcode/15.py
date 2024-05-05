""" 3SUM problem """

nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    nums = sorted(nums)

    result = []
    for i in range(len(nums)):
        target = -nums[i]
        l = i + 1
        r = len(nums) - 1
        if i>0 and nums[i] == nums[i-1]:
            continue
    
        while(l < r):
            if nums[l] + nums[r] == target:
                result.append([nums[i], nums[l], nums[r]])
            
                l = l+1
                while l<r and nums[l] == nums[l-1]:
                    l+=1
            elif nums[l] + nums[r] < target:
                l+=1
            else:
                r-=1
        
    return result

output = threeSum(nums)
print(output)
        