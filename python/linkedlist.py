## this is code for making code for linkedlist

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next
    
    def hasNextNode(self):
        return self.next!=None


class LinkedList:

    def __init__(self, node = None):
        self.length = 0
        self.head = node

    def getLengthLinkedList(self):
        current = self.head
        count = 0
        while current!=None:
            count+=1
            current = current.next
        return count
    
    def displayAllElement(self):
        current =  self.head
        print("Displaying all element")
        while current!=None:
            print("Element are", current.data)
            current = current.next


    def insertAtBeginnig(self, data):
        newNode = Node()
        newNode.data = data
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.data = data
        if self.head == None:
            head = newNode
        else:
            current = self.head
            while current.next!=None:
                current = current.next
            current.next = newNode

    def insertAtGivenPoint(self, data, n):
        newNode = Node()
        newNode.data = data
        totallengthlist = self.getLengthLinkedList()
        if totallengthlist==0:
            self.insertAtBeginnig(data)
        elif n > totallengthlist:
            print("Given index is out of range")
        elif n==totallengthlist:
            self.insertAtEnd(data)
        else:
            index=1
            current = self.head
            while index < n-1:
                index+=1
                current = current.next
            newNode.next = current.next
            current.next = newNode



# newNode = Node()
# head = None
# print(newNode.data)
llobj = LinkedList()

data = 4
llobj.insertAtBeginnig(data)
data=3
llobj.insertAtBeginnig(data)
data=6
llobj.insertAtEnd(data)
data=8
llobj.insertAtEnd(data)
llobj.displayAllElement()
data = 5
llobj.insertAtGivenPoint(data, 3)
llobj.displayAllElement()


# newNode.data = data
