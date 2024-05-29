""" Search in rotated search array """

from typing import List
import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l<r:
            mid = (l+r) // 2
            if nums[mid]==target:
                return mid+1
            elif nums[l] <= nums[mid] and target <= nums[mid]:
                r = mid-1
            elif nums[mid] <= target and target <= nums[r]:
                low = mid+1
            else:
                r = mid-1

        return -1  


s = Solution()

# nums = [4,5,6,7,0,1,2]
# target = 0
# nums = [4,5,6,7,0,1,2]
# target = 3
nums = [2,5,4,0]
target = 2
out = s.search(nums, target)
print(out)
