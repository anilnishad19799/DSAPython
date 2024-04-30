""" from book cracking the coding interview """

string  = "anil"
from collections import defaultdict

def IsUnique(string):
    setstring = set(string)
    hash = defaultdict(int)

    if len(setstring) != len(string):
        return False

    for i in string:
        hash[i] += 1

        if hash[i] > 1:
            return False
    print(hash)
    return True

output = IsUnique(string)
print(output)