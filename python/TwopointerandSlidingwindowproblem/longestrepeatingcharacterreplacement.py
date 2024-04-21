""" Given Task 
    s = AABABBA, K=2
    find longest substring with replacing k character and get repeating element having maxlength

"""
s = "AAABABBA"
k = 2
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