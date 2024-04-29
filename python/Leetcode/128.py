""" Loongest common subsequence """


# def longestsubsequence():
#     nums = [0,3,7,2,5,8,4,6,0,1]

#     setnums = set(nums)

#     hash = {i:0 for i in setnums}

#     for i in setnums:
#         hash[i] = 1


#     maxcount = 0
#     for i in setnums:
#         count = 0
#         cnt = i

#         while cnt in hash:
#             cnt+=1
#             count+=1
        
#         if maxcount < count:
#             maxcount = count
    
#     return maxcount


def longestsubsequence():

    # nums = [0,3,7,2,5,8,4,6,0,1]
    nums = [100,4,200,1,3,2]

    setnums = set(nums)
    setnums = sorted(setnums)    
    
    hash = {i:0 for i in setnums}
    for i in setnums:
        hash[i] = 1

    maxcount = 0
    count = 1
    for i in range(len(setnums)):
        if (setnums[i] + 1) in hash:
            count+=1
        else:
            count = 1
        
        if maxcount < count:
            maxcount = count
    
    return maxcount

output = longestsubsequence()
print(output)