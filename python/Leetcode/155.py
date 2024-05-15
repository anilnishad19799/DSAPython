class MinStack:

    def __init__(self):
        # pass
        self.stack = []
        self.minvallist = []

    def push(self, val: int) -> None:
        # pass
        self.stack.append(val)
        if not self.minvallist or val <= self.minvallist[-1]:
            self.minvallist.append(val) 

    def pop(self) -> None:
        # pass
        
        if self.stack.pop() == self.minvallist[-1]:
            self.minvallist.pop()


    def top(self) -> int:
        # pass
        return self.stack[-1]

    def getMin(self) -> int:
        # pass
        return self.minvallist[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()