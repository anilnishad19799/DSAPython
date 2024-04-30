""" Given Task 
    arr = bbacba
    first all substring having all threee character 
    in above example let say bbac, bac, bbacb, bbacba, and many many more there are substring having with three character
"""

""" brute force approach """
arr = "bbacba"
maxlen = 0
n = len(arr)


cnt = 0
for i in range(n):
    hashmap = {i:0 for i in range(3)}
    for j in range(i, n):
        hashmap[ord(arr[j]) - ord('a')] = 1

        # if (hashmap[0] + hashmap[1] + hashmap[2])==3:
        #     cnt +=1

        if (hashmap[0] + hashmap[1] + hashmap[2])==3:
            cnt += (n-j)
            break


print(cnt)

""" Better and optimal approach"""
r = 0
cnt = 0
hashmap = {i:-1 for i in range(3)}
n = len(arr)

for i in range(n):
    hashmap[ord(arr[i]) - ord('a')] = i
    if hashmap[0]!=-1 and hashmap[1]!=-1 and hashmap[2]!=-1:
        cnt = cnt + (1 + min(hashmap[0], hashmap[1], hashmap[2]))

print(cnt)