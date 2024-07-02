"""finding kth largest elemtn from Array"""

from typing import List
import heapq

""" Solution 1 using sorted way """
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         sortedsetvalue = sorted(nums)
#         output = sortedsetvalue[-k]
#         return output
    

""" Solution 2 using heap """
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for i in nums:
            heapq.heappush(maxheap, i)

            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        return maxheap[0]


s = Solution()
# nums = [3,2,3,1,2,4,5,5,6]
# k= 4

nums = [2,3,1,1,5,5,4]
k = 3
# nums = [3,2,1,5,6,4]
# k = 2

output = s.findKthLargest(nums, k)
print(output)