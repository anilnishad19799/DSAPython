class CircularQueue:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.A = [None] * capacity
        self.rear = -1
        self.front = -1

    def enqueue(self, data):

        if self.rear == self.front:
            print("Queue Overflow")
            return

        if self.rear == self.capacity:
            self.rear = 0

        self.rear = self.rear + 1
        self.A[self.rear] = data

    def deque(self):

        if self.front == self.rear+1:
            print("Stack Underflow")

        if self.front == self.capacity:
            self.front = 0

        deletedelement  = self.A[self.front]
        self.front = self.front + 1

    def display(self):

        iterfront = self.front
        while(iterfront < self.rear):
            print("element are ", iterfront)
            iterfront = iterfront+1

queue = CircularQueue(10)
queue.enqueue("First")
queue.enqueue("Second")

    
