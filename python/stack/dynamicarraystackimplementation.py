import random
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

stack = DynamicArrayStack(20)
print("*"*100)
print("push")
for i in range(26):
    stack.push(random.randint(1,1000))

print("*"*100)
print("peep")
stack.peep()

print("*"*100)
print("pop")
for i in range(12):
    stack.pop()
    