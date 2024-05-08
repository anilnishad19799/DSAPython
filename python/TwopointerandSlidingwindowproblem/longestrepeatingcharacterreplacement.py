""" Given Task 
    s = AABABBA, K=2
    find longest substring with replacing k character and get repeating element having maxlength

"""
# s = "AAABABBA"
# k = 2
s = "AABABBA"
k = 1
maxlen = 0
n = len(s) - 1
for i in range(n):
    rcr = 0
    for j in range(i,n):
        if ord(s[j]) != ord(s[i]):
            rcr +=1

        if rcr <= k:
            maxlen = max(maxlen, j-i+1)
        else:
            break

print(maxlen)

""" Better approach """
l,r,maxlen,n = 0,0,0, len(s)-1
rcr = 0

while(r<n):
    if ord(s[r])!= ord(s[l]):
        rcr +=1
    
    while rcr > k:
        if ord(s[r])!= ord(s[l]):
            rcr-=1
        l+=1

    if rcr <=k:
        maxlen = max(maxlen, r-l+1)

    r+=1

print(maxlen)



""" As per youtube answer given approach"""
""" Brute force approach """

n = len(s)
maxf = 0
for i in range(n):
    hash = {i:0 for i in range(26)}
    for j in range(i, n):
        hash[ord(s[j]) - ord('A')] +=1
        maxf = max(maxf, hash[ord(s[j])- ord('A')])
        change = (j - i + 1) - maxf

        if change <=k:
            maxlen = max(maxlen, j-i+1)
        else:
            break
print(maxlen)


""" Optimal solution """

l,r,maxlen,maxf = 0,0,0,0
hash = {i:0 for i in range(26)}
n = len(s)
while r < n:
    hash[ord(s[r]) - ord("A")] +=1
    maxf = max(maxf, hash[ord(s[r])- ord('A')])

    if (r-l+1) - maxf > k:
        hash[ord(s[r])-ord('A')] -=1
        maxf = 0
        l+=1

    if (r-l+1) - maxf <= k:
        maxlen = max(maxlen, r-l+1)

    r+=1
print(maxlen)