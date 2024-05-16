def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []
    
    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Discard the '('
        else:  # Operator
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

# Test the function
infix_expression = "a+b*c-(d/e+f)*g"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)



postfixoutput = []
stack = []
precedenceoperator = {"-":1, "+":1, "*":2, "/":2, "^":3}
expression = "a+b*c-(d/e+f)*g"
for char in expression:
    if char.isalnum():
        postfixoutput.append(char)
    elif char is "(":
        stack.append(char)
    elif char is ")":
        while stack and stack[-1]!="(":
            postfixoutput.append(stack.pop())

        stack.pop()
    else:
        while precedenceoperator[char] < precedenceoperator[stack[-1]]:
            postfixoutput.append(stack.pop())

        stack.append(char)
    
    while stack:
        postfixoutput.append(stack.pop())

print(postfixoutput)

