""" replace ' ' with %20 string"""

def Urlify(s1, replacestr):
    # finalstring = s1.replace(' ', replacestr)

    finalstring = ''
    for i in s1:
        if i == ' ':
            # pass
            finalstring+=replacestr
        else:
            finalstring+=i
        
        if len(finalstring) == len(s1):
            return finalstring

    return finalstring

s1 = 'a ni l    '
relacestr = "%20"
output = Urlify(s1, relacestr)
print(output)