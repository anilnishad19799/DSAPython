from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        for i in s:
            hash1[i]+=1

        for j in t:
            hash2[j]+=1

        if len(hash2) > len(hash1):
            temp1 = hash2
            temp2 = hash1
        else:
            temp1 = hash1
            temp2 = hash2
        
        for k in temp1.keys():
            if k in temp2.keys():
                if temp1[k] != temp2[k]:
                    return False
            else:
                return False

        return True
    

    """
    Some better approach
    
    count = defaultdict()
    for i in s:
        count[x]+=1    
    
    for i in t:
        count[x]--
    
    for k,v in count.items:
        if v!=0:
            return False

    return True
        
            
    """
    

soultion =  Solution()
output = soultion.isAnagram("AB", "AB")
print(output)