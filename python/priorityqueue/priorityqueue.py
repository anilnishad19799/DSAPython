class PriorityQueue:
    def _init_(self):
        self.heaplist = [0]
        self.size = 0

    def swap(self, i):
        temp = self.heaplist[i//2]
        self.heaplist[i//2] = self.heaplist[i]
        self.heaplist[i] = temp
    
    def insertHeapify(self, i):
        while i//2 > 0:
            if self.heaplist[i] > self.heaplist[i//2]:
                self.swap(i)
            i = i//2


    def insert(self, data):
        self.size = self.size+1
        self.heaplist.append(data)
        self.insertHeapify(self.size)
        print(self.heaplist)



    
    def maximumValueindex(self, i):
        if i*2 > self.size:
            return 2*i
        else:
            if self.heaplist[2*i] > self.heaplist[2*i+1]:
                return 2*i
            else:
                return (2*i) + 1    


    def deleteHeapify(self, i):
        while i*2 < self.size:
            minindex = self.maximumValueindex(i)
            temp = self.heaplist[minindex]
            self.heaplist[minindex] = self.heaplist[i]
            self.heaplist[i] = temp
            i = minindex

    """ It is always the case where root node is deleted first in priority queue"""
    def delete(self):
        self.heaplist[1] = self.heaplist[self.size]
        self.heaplist.pop()
        self.size = self.size - 1
        self.deleteHeapify(1)
        print(self.heaplist)



priorityqueueobj = PriorityQueue()
priorityqueueobj.insert(20)
priorityqueueobj.insert(30)
priorityqueueobj.insert(40)
priorityqueueobj.insert(10)
priorityqueueobj.delete()