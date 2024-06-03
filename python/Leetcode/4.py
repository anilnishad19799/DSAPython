import numpy as np
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        i = len(nums1)

        if i%2 == 1:
            return nums1[i//2]
        else:
            return (nums1[(i//2)-1] + nums1[i//2]) / 2
    
s = Solution()
nums1 = [1,2]
nums2 = [3,4]
out = s.findMedianSortedArrays(nums1, nums2)
print(out)