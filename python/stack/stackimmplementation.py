import random

class Stack:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.top = -1
        self.A = [None] * capacity        

    def push(self, data):
        if self.capacity == self.top:
            print("Stack Overflow")
            return

        self.top+=1
        self.A[self.top] = data

    def pop(self):
        if self.top ==-1:
            print("Stack Underflow")
            return
        
        print("data deleted is ", self.A[self.top])
        self.top-=1

    def peep(self):
        if self.top==-1:
            print("Stack Underflow")
        for i in range(self.top+1):
            print(self.A[i])

stack = Stack(20)
for i in range(10):
    stack.push(random.randint(1,21))

stack.peep()

for i in range(12):
    stack.pop()
    