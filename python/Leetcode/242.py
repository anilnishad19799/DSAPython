from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        for i in s:
            hash1[i]+=1

        for j in t:
            hash2[j]+=1

        if len(hash2) > len(hash1):
            hash
        
        for k in hash1.keys():
            if k in hash2.keys():
                if hash1[k] != hash2[k]:
                    return False
            else:
                return False

        return True
            

# SULUTIO ISUE = "AB", "A"