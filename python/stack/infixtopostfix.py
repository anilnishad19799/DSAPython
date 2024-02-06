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

    def peep(self):
        if self.top == -1:
            print("stack underflow")

        for i in range(self.top+1):
            print(self.A[i])


stack = DynamicArrayStack()
""" Making fucntion for converting infix to postfix expression"""

precedenceoperator = {"^":5, "*":4, "/":4, "+":3, "-":3, "(":2}
mapping = {")":"("}
character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
postfixexroession = []

def infixToPostfixConversion(expression):
    for express in expression:
        if express in character or express in number:
            postfixexroession.append(express)
        elif express == "(":
            stack.push(express)
        elif express == ")":
            popelement = stack.pop()
            while mapping[express]!=popelement:
                postfixexroession.append(popelement)
                popelement = stack.pop()

        else:
            popelement = stack.pop()
            while precedenceoperator[express] <= precedenceoperator[popelement]:
                postfixexroession.append(popelement)
                popelement = stack.pop()
            postfixexroession.append(popelement)
            stack.push(express)

    return postfixexroession


expression = "A*B+(C/D)-E*F+G^H"
output = infixToPostfixConversion(expression)
print(output)
