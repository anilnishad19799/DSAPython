""" Longest repeating character replacement"""
from collections import defaultdict
# s = "ABAB"
s = "AABABBA"
k = 1

def characterReplacement(s, k):
    l,r = 0,0
    n = len(s)
    maxf, maxcount = 0,0

    hash = defaultdict(int)
    while r < n:
        hash[s[r]]+=1
        
        maxf = max(maxf,hash[s[r]])

        if (r-l+1)-maxf > k:
            hash[s[l]]-=1
            maxf=0
            l+=1

        if (r-l+1) - maxf <= k:
            maxcount = max(maxcount, r-l+1)

        
        r+=1
    
    return maxcount

output = characterReplacement(s, k)
print(output)
    # print(hash)