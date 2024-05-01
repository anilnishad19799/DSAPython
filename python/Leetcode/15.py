""" 3 Sum """
from collections import defaultdict, Counter
# nums = [-1,0,1,2,-1,-4]
nums = [3,-2,1,0]
# nums = [1,2,-2,-1]

triplesum = []
l = 0

length =  len(nums)
while l  < length - 2:
    target = -nums[l]
    hash  = Counter(nums[l+1:length])
    print("l",l)
    for i in range(l+1, length-1):
        curr = target - nums[i]
        if curr in hash:
            sortlist = sorted([curr, nums[l], nums[i]])
            if sortlist not in triplesum:
                triplesum.append(sortlist)
    l+=1


print(triplesum)
