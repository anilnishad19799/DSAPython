""" Group anagram"""
from typing import List
from  collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash = defaultdict(list)
        for i in strs:
            ss = ''.join(sorted(i))
            hash[ss].append(i)
        
        return hash.values()

sol =  Solution()
output = sol.groupAnagrams(strs)
print(output)