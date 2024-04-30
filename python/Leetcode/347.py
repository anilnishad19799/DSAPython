""" Top K frequent element """
from typing import List
from collections import defaultdict
import heapq
# nums = [1,1,1,2,2,3]
# k = 2

nums = [1,2]
k = 2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums)==k:
            return list(set(nums))
    
        hash = defaultdict(int)
        for i in nums:
            hash[i]+=1

        heap = [(-freq, num) for num,freq in hash.items()]
        heapq.heapify(heap)

        print("heap")

        topk = [heapq.heappop(heap)[1] for _ in range(k)]

        return topk        



sol =  Solution()
output = sol.topKFrequent(nums, k)
print(output)