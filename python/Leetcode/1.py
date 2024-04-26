from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash =  defaultdict()
        n = len(nums) - 1
        for i in range(n):
            hash[nums[i]] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in  hash and hash[comp]!=i:
                return [i, hash[comp]]
        
        return []
    
ts = Solution()
nums = [3,3]
target = 9
output = ts.twoSum(nums, target)
print(output)