from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        
    def add(self, val: int) -> int:
        self.nums.append(val)

        # descendsort = sorted(self.nums, reverse=True)
        # print(descendsort)
        for index, allval in enumerate(self.nums):
            if allval >= val:
                self.nums.insert(index, val)
            
        descendsort = self.nums[self.k-1]
        return descendsort[self.k-1]


k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
val = 3
param_1 = obj.add(val)
print(param_1)