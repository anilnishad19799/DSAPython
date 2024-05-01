""" Longest consecutive subsequence"""

from collections import defaultdict

def longestsubsequence():
    # nums = [100,4,200,1,3,2]
    # nums = [0,3,7,2,5,8,4,6,0,1]
    # nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    nums = [-8,-4,9,9,4,6,1,-4,-1,6,8]
    setnum = set(nums)

    hash = defaultdict(int)
    minvalue = 1000000
    for i in setnum:
        hash[i]=1
        if i < minvalue:
            minvalue = i

    print(hash)
    count = 1
    cnt = minvalue
    maxcount = 0
    for i in range(len(hash)):
        print(i)
        cnt+=1
        if cnt in hash:
            # print(cnt)
            # print("cnt in hash")
            count+=1
        else:
            if maxcount < count:
                maxcount = count
            count = 0

        if maxcount < count:
                maxcount = count
    
    return maxcount

output = longestsubsequence()
print(output)



