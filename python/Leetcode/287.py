""" FInd duplicate number from list """

from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = defaultdict(int)

        for val in nums:
            if hash[val] == 1:
                return val
            hash[val]+=1

s = Solution()
# nums = [1,3,4,2,2]
# nums = [3,1,3,4,2]
nums = [3,3,3,3,3]
output = s.findDuplicate(nums)
print(output)