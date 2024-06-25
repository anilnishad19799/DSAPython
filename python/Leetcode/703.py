from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        
    def add(self, val: int) -> int:
        # descendsort = sorted(self.nums, reverse=True)
        # print(descendsort)
        index = 0
        for allval in self.nums:
            if val >=allval:
                self.nums.insert(index, val)
                break
            index+=1

        descendsort = self.nums[self.k-1]
        return descendsort


k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
val = 3
param_1 = obj.add(val)
print(param_1)