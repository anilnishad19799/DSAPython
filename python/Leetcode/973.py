""" Closest pointo to (0,0) """


import heapq
import math
from  typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for val in points:
            sqrtvalue = ((val[0]- 0)**2 + (val[1]-0)**2)
            self.add(maxheap, val,sqrtvalue, k)
        
        return [point for _, point in maxheap]
    
    def add(self, heap, points, sqrtval, k):
        if len(heap) < k:
            heapq.heappush(heap, (-sqrtval, points))
        elif sqrtval < -heap[0][0]:
            print(sqrtval, -heap[0][0])
            heapq.heapreplace(heap, (-sqrtval, points))
        print(heap)
 
s = Solution()
# points = [[1,3],[-2,2]]
# k = 1
points = [[3,3],[5,-1],[-2,4]]
k = 2
output = s.kClosest(points, k)
print(output)

# import heapq
# from typing import List

# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         # Use a max-heap to store the k closest points
#         max_heap = []
        
#         for val in points:
#             # Calculate the squared distance from the origin
#             sqrtvalue = (val[0] ** 2 + val[1] ** 2)
#             # Add the point to the heap
#             self.add(max_heap, val, sqrtvalue, k)
        
#         # Extract the points from the heap
#         return [point for _, point in max_heap]
    
#     def add(self, heap, point, dist, k):
#         if len(heap) < k:
#             heapq.heappush(heap, (-dist, point))  # Use negative distance for max-heap behavior
#         elif dist < -heap[0][0]:
#             heapq.heapreplace(heap, (-dist, point))  # Replace the farthest point if the current one is closer

# s = Solution()
# # points = [[3, 3], [5, -1], [-2, 4]]
# # k = 2
# points = [[1,3],[-2,2]]
# k = 1
# output = s.kClosest(points, k)
# print(output)
