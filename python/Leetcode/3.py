class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r,maxlen,maxf = 0,0,0,0
        hash = {i:0 for i in range(26)}
        n = len(s)
        while r < n:
            hash[ord(s[r]) - ord("A")] +=1
            maxf = max(maxf, hash[ord(s[r])- ord('A')])

            if (r-l+1) - maxf >= k:
                hash[ord(s[r])-ord('A')] -=1
                maxf = 0
                l+=1

            if (r-l+1) - maxf <= k:
                maxlen = max(maxlen, r-l+1)

            r+=1
        return maxlen