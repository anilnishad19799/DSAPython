""" Last Stone Weight Problem statement """


from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        negativelist = [-1*val for val in stones]
        heapq.heapify(negativelist)

        while len(negativelist)>1:
            firstval =  heapq.heappop(negativelist)
            secondval = heapq.heappop(negativelist)
            heapq.heappush(negativelist, firstval-secondval)
        
        if len(negativelist)==0:
            return 0
        else:
            return -1*negativelist[0]


solutionobj = Solution()
stones = [2,7,4,1,8,1]
output = solutionobj.lastStoneWeight(stones)
print(output)
