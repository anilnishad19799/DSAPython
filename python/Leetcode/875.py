""" KOKO eating banana """
""" Take help from youtube to solve """

import math
from typing import List

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


piles = [3,6,7,11]
h = 8

# piles = [30,11,23,4,20]
# h = 5

# piles = [30,11,23,4,20]
# h = 6

s = Solution()
output = s.minEatingSpeed(piles, h)
print(output)