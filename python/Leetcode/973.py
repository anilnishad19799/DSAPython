""" Closest pointo to (0,0) """


import heapq
import math
from  typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        outputlist = []
        for val in points:
            sqrtvalue = math.sqrt((val[0]- 0)**2 + (val[1]-0)**2)
