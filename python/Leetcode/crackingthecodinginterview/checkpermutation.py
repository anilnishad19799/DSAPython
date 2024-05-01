""" check one string is permutation of another """
from itertools import permutations
from collections import defaultdict


# string = 'abc'


# # """ time complexity is  Big 0(N * N!)"""
# def checkpermutations(str1, str2):
    
#     if len(str1) < len(str2):
#         minstr = str1
#         maxstr = str2
#     else:
#         minstr = str2
#         maxstr = str1
    
#     minpermuatationslist = [''.join(str) for str in permutations(minstr)]

#     for i in minpermuatationslist:
#         if i in str2:
#             return True
    
#     return False

# # str1 = 'ab'
# # str2 = 'bva'

# str1 = "abcdxabcde"
# str2 = "abcdeabcdx"
# output = checkpermutations(str1, str2)
# print(output)

""" Some better approach """

# def checkpermutations(s1, s2):

#     if len(s1) > len(s2):
#         return False 
        
#     hash = defaultdict(int)

#     for i in s1:
#         hash[i]+=1
    
#     print("hash",hash)
#     l,r = 0, len(s1)
#     while(r<=len(s2)):
#         hash2 = defaultdict(int)
#         for i in s2[l:r]:
#             hash2[i]+=1
#         print("hash2",hash2)
        
#         count = 0
#         for k,v in hash.items():
#             if k in hash2 and hash2[k] == v:
#                 print("k",k,"v",v,"hash2[k]",hash2[k], "count", count)
#                 count+=v
#                 if count == len(s1):
#                     return True
#             else:
#                 break

#         l+=1
#         r+=1

#     return False



# str1 = "abcdxabcde"
# str2 = "abcdeabcdx"

# # str1 = 'ab'
# # str2 = "eidboaoo"

# output = checkpermutations(str1, str2)
# print(output)

"""
Soultion if anyone is permutation of other

    # if len(str1) < len(str2):
    #     minstr = str1
    #     maxstr = str2
    # else:
    #     minstr = str2
    #     maxstr = str1
    
    # hash = defaultdict(int)

    # for i in minstr:
    #     hash[i]+=1
    
    # l,r = 0, len(minstr)-1
    # while(r<len(maxstr)):
    #     hash2 = defaultdict(int)
    #     for i in maxstr[l:r+1]:
    #         hash2[i]+=1
        
    #     count = 0
    #     for k,v in hash.items():
    #         if k in hash2 and hash2[k] == v:
    #             count+=1
    #             if count == len(minstr):
    #                 return True
    #         else:
    #             break

    #     l+=1
    #     r+=1

    # return False
"""

""" Best approach"""
from collections import Counter
def checkpermutations(s1, s2):
    if len(s1) > len(s2):
        return False 
    hash1counter = Counter(s1)

    if len(s1) == len(s2):
        if Counter(s1) == Counter(s2):
            return True
        else:
            False

    l,r = 0, len(s1)
    while(r<=len(s2)):
        hash2counter = Counter(s2[l:r])
        if hash1counter == hash2counter:
            return True
        l+=1
        r+=1

    return False


str1 = "ab"
str2 = "eidbaoo"

output = checkpermutations(str1, str2)
print(output)
