""" permutation of it and hceck it is palidrome or not"""

from itertools import permutations

def checkpalindromeandpermution(str):
    str = str.lower()
    permutationslist = [''.join(i) for i in permutations(str)]

    # print(permutationslist)
    listofall = []
    listofallwithout = []
    for i in permutationslist:
        strip1 = i.replace(' ','')
        if strip1 == strip1[::-1]:
            
            if strip1 not in listofallwithout:
                listofall.append(i)
            listofallwithout.append(strip1)

    return listofall

str = 'nii'

output = checkpalindromeandpermution(str)
print(output)

