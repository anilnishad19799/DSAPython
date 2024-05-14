class MinStack:

    def __init__(self):
        # pass
        self.stack = []
        self.minval = 10000
        self.minvallist = []

    def push(self, val: int) -> None:
        # pass
        self.stack.append(val)
        if self.minval >= val:
            self.minval = val
            self.minvallist.append(val)
        else:
            self.minvallist.insert(0, val)

    def pop(self) -> None:
        # pass
        popvalue = self.stack.pop()
        if popvalue == self.minvallist[-1]:
            self.minvallist.pop()


    def top(self) -> int:
        # pass
        return self.stack[-1]

    def getMin(self) -> int:
        # pass
        return self.minvallist[-1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)

min = minStack.getMin() # return -3
print(min)
print("*"*100)

# minStack.pop()
topval = minStack.top()    # return 0
print(topval)

minval = minStack.getMin() # return -2
print(minval)