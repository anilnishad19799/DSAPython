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

        deletedelement = self.A[self.top]
        if self.top < self.capacity // 2:
            self.capacity = self.capacity // 2
            newArray = [None] * self.capacity

            for i in range(self.top):
                newArray[i] = self.A[i]

            self.A = newArray

        self.top = self.top - 1
        return deletedelement

    def peep(self):
        if self.top == -1:
            print("stack underflow")

        for i in range(self.top+1):
            print(self.A[i])

stack = DynamicArrayStack()

""" First Approach"""
def checkValidExpression(express):
    mapping = {"}":"{",")":"(","]":"["}

    for symbol in express:
        if symbol in mapping:
            topelement = stack.pop()
            if mapping[symbol] != topelement:
                return False
        else:
            stack.push(symbol)
    return True

# print(checkValidExpression(")[]("))

stack = DynamicArrayStack()
def checkValidExpressionSecondApproach(express):

    openingsymbol = ["(","{","["]
    closingsymbol = ["}","]",")"]
    validcount = 0

    for symbol in express:
        print("symbol", symbol)
        if symbol in openingsymbol:
            stack.push(symbol)
            validcount+=1

        if symbol in closingsymbol:
            stack.pop()
            validcount-=1
        
        if validcount<0:
            return "Expression is not valid"


    if validcount==0:
        return "Expression is valid"
    else:
        return "Expression is not valid"

print(checkValidExpressionSecondApproach(")[]("))


        
