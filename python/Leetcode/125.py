""" valid palindrome """
import re
def isPalindrome(s: str) -> bool:

    # s = re.sub(r'[\W_]', '', s)

    l,r = 0, len(s)-1
    while(l<r):

        while not s[l].isalnum() and l < r:
            l+=1
        while not s[r].isalnum() and l < r:
            r-=1
        
        if s[l].lower() != s[r].lower():
            return False
        l+=1
        r-=1
    return True

s = ".,"

output = isPalindrome(s)
print(output)