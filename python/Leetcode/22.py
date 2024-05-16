"""from itertools import permutations

def generate_permutations(n):
    s = '(' * n + ')' * n
    all_permutations = set(permutations(s))
    unique_permutations = [''.join(p) for p in all_permutations]
    return unique_permutations

n = 5
permutations_list = generate_permutations(n)

# Print the results
count = 0
finalstack = []
for p in permutations_list:
    stack = []
    validparenthesis = True
    # print(p)
    if p.startswith(")"):
        validparenthesis = False
    else:
        # print(p)
        for i in p:
            if i == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    validparenthesis = False
                    break
    if validparenthesis:
        finalstack.append(p)

        
print(finalstack)"""

