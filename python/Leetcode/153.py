""" find minimum in sorted array """

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            print(l,r)
            if nums[l] <= nums[r]:
                r = ((l + r) // 2)
            else:
                l = ((l + r) // 2)

        if nums[l] < nums[r]:
            return nums[l]
        else:
            return nums[r]            


s = Solution()

# nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
# nums = [11,13,15,17]
# nums = [2,1]
# nums = [3,1,2]
nums = [2,3,1]
out = s.findMin(nums)
print(out)
