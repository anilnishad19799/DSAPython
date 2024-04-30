""" Implement stack using linkedlist"""

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
    
class StackUsingLinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        newNode = Node()
        newNode.data = data
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head == None:
            return "No element to delete"

        curr = self.head
        curr = curr.next
        self.head.next = None
        self.head = curr

    def peep(self):
        if self.head == None:
            return "No Element to display"  
        
        curr = self.head
        while curr!=None:
            print("Node data ", curr.data)
            curr = curr.next

sll = StackUsingLinkedList()
sll.push(4)
sll.push(5)
sll.peep()
sll.pop()
print("peep")
sll.peep()