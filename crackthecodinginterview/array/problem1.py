## implement an algorithm to determine if a string has all unique character

'''first approach using worst case approach using n square time complexity'''

'''
test_string = 'abvcdf'

def FirstApproach(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False, string[i]
    
    return True, 0

output, character = FirstApproach(test_string)
if output:
    print("all character is unique")
else:
    print("duplicate character in string", character)

'''


"""Second approach takes time complexity nlogn due to sorting approach"""

'''
test_string = 'abcdfv'

def secondApproach(string):
    sortedstring = sorted(string)
    for i in range(len(sortedstring)-1):
        if sortedstring[i]==sortedstring[i+1]:
            return False, sortedstring[i]
        
    return True, 0

output, character = secondApproach(test_string)
if output:
    print("all character is unique")
else:
    print("duplicate character in string", character)

'''

"""Third approach using hash table time complexity (n)"""

def get_hash(key):
    return ord(key)

test_string = 'qwertyuiopq'
unique_dict = {}

def thirdApproach(string):
    for i in string:
        charactertonumber = get_hash(i)
        gethasvalue = charactertonumber % 26
        if gethasvalue in unique_dict.keys():
            return False, i
        
        unique_dict[gethasvalue] = i

    return True, 0

output, character = thirdApproach(test_string)

if output:
    print("all character is unique")
else:
    print("duplicate character in string", character)
