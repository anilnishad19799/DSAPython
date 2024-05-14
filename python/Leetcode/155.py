class MinStack:

    def __init__(self):
        # pass
        self.stack = []

    def push(self, val: int) -> None:
        # pass
        self.stack.append(val)

    def pop(self) -> None:
        # pass
        self.stack.pop()

    def top(self) -> int:
        # pass
        return self.stack[-1]

    def getMin(self) -> int:
        # pass
        print(self.stack)
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

minval = minStack.getMin() # return -3
print(minval)
print("*"*100)

minStack.pop()
topval = minStack.top()    # return 0
print(topval)

minval = minStack.getMin() # return -2
print(minval)