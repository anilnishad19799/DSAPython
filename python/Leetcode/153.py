""" find minimum in sorted array """

from typing import List
import math

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
    
        while l < r:
            print(l,r)
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]          


s = Solution()

nums = [1]
nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
# nums = [11,13,15,17]
# nums = [2,1]
# nums = [3,1,2]
# nums = [2,3,1]
# nums = [5,1,2,3,4]
out = s.findMin(nums)
print(out)
