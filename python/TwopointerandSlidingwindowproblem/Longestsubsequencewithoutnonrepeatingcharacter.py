"""
    s = cadbzabcd
    find maximum subsequence count having non repreating character
    output = 5
"""

""" Brute force approach 
    find all substring and compare everytime to it maxlen value
    also used here hash mapping technique
"""

s = "cadbzabcd"
lens = len(s) - 1
maxlen = 0
for i in range(lens):
    hashmap = {i:0 for i in range(256)}
    for j in range(lens):
        if hashmap[ord(s[j])] == 1:
            break

        maxlen = max(maxlen, j-i+1)
        hashmap[ord(s[j])] = 1

print(maxlen)

""" Optimal approach using two pointer and sliding windows"""

s = "cadbzabcd"
l = 0
r = 0
hashmap = {i:-1 for i in range(256)}
maxlen = 0
lens = len(s) - 1
while r < lens:

    if hashmap[ord(s[r])] != -1:
        if hashmap[ord(s[r])] >= l:
            l = hashmap[ord(s[r])] + 1

    len = r-l+1
    maxlen = max(maxlen, len)
    hashmap[ord(s[r])] = r
    r+=1

print(maxlen)