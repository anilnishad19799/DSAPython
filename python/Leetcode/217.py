""" 217. Contains Duplicate """

""" Soultion """

from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr_set = set(nums)
        if len(arr_set) != len(nums):
            return True
        else:
            return False

        """
        hash = defaultdict(int)

        for num in nums:
            hash[num] += 1
            if hash[num] > 1:
                return True
        return False

        """