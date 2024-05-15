""" Here Stack Implementation"""
class DynamicArrayStack:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.A = [None] * capacity
        self.top = -1
    

    def resize(self):
        self.capacity = self.capacity * 2
        newArray = [None] * self.capacity
        for i in range(self.top):
            newArray[i] = self.A[i]
        self.A = newArray

    def push(self, data):
        self.data = data
        if self.capacity == self.top+1:
            print("Trying to resize ")
            self.resize()

        self.top = self.top + 1
        self.A[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")

        if self.top < self.capacity // 2:
            self.capacity = self.capacity // 2
            newArray = [None] * self.capacity

            for i in range(self.top):
                newArray[i] = self.A[i]

            self.A = newArray

        print("deleted element are ", self.A[self.top])

        self.top = self.top - 1

        return self.A[self.top+1]

    def peep(self):
        if self.top == -1:
            print("stack underflow")

        for i in range(self.top+1):
            print(self.A[i])

    def gettop(self):
        print("top called", self.top)
        return self.A[self.top]

stack = DynamicArrayStack()

""" Making fucntion for converting infix to postfix expression"""

def infixToPostfixConversion(expression):
    postfixexroession = []
    precedenceoperator = {"^":5, "*":4, "/":4, "+":3, "-":3, "(":2}
    mapping = {")":"("}
    character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"


    print("*"*100)
    print(stack.gettop())
    print("$"*100)
    for express in expression:
        print(express)
        if express in character or express in number:
            postfixexroession.append(express)
        elif express == "(":
            stack.push(express)
        elif express == ")":
            popelement = stack.pop()
            # print("popel;ement", popelement)
            while mapping[express]!=popelement:
                postfixexroession.append(popelement)
                popelement = stack.pop()

        # else:
        #     popelement = stack.top()
        #     while precedenceoperator[express] <= precedenceoperator[popelement]:
        #     # while precedenceoperator[express] <= stack[-1]:
        #         postfixexroession.append(stack.pop())
        #         popelement = stack.top()
        #     # postfixexroession.append(popelement)
        #     stack.push(express)

            if not stack.gettop():
                stack.push(express)
            else:
                while precedenceoperator[express] <= precedenceoperator[stack.gettop()] and stack.gettop():

                    popelement = stack.pop()
                    postfixexroession.append(popelement)
                
                stack.push(express)

    while stack.gettop():
        postfixexroession.append(stack.pop())        

    return postfixexroession


# expression = "A*B+(C/D)-E*F+G^H"
expression = "A+B-C"

output = infixToPostfixConversion(expression)
print(output)


