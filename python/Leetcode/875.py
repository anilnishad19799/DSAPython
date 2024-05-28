""" KOKO eating banana """
""" Take help from youtube to solve """

import math
from typing import List


""" Brute Force Approach """
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mink = 1000000
        for k in range(1, max(piles)+1):
            totalhours = 0
            for i in piles:
                totalhours+=math.ceil(i / k)

            if totalhours <= h and mink > k:
                mink = k

        return mink


""" Binary Search Approach """
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mink = 1000000
        l = 1
        r = max(piles)
        while l <=  r:
            mid = (l+r) // 2
            totalhours = 0
            for i in piles:
                totalhours+=math.ceil(i / mid)

            # if totalhours <= h and mink > mid:
            #     mink = mid

            if totalhours <= h:
                r = mid - 1
                mink = mid;
            else:
                l = mid+1

        return mink

# piles = [3,6,7,11]
# h = 8

# piles = [30,11,23,4,20]
# h = 5

# piles = [30,11,23,4,20]
# h = 6

piles =[1000000000]
h = 2

s = Solution()
output = s.minEatingSpeed(piles, h)
print(output)