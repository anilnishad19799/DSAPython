class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next
    
    def setPrev(self, prev):
        self.prev = prev

    def getPrev(self):
        return self.prev
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def getLengthLinkedList(self):
        count = 0

        curr = self.head
        while curr!=None:
            count+=1
            curr = curr.next

        return count

    def insertAtFirst(self, data):
        newNode = Node(data, None, None)
        if self.head == None:
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
    

    def insertAtEnd(self, data):
        newNode = Node(data, None, None)
        
        if self.head == None:
            self.head = newNode

        curr = self.head
        while curr.next!=None:
            curr = curr.next

        curr.next = newNode
        newNode.prev = curr

    def insertAtGivenIndex(self, data, index):
        newNode = Node(data, None, None)

        if self.head == None:
            self.head = newNode

        length_LinkedList = self.getLengthLinkedList()
        if length_LinkedList < index:
            return "Index is more than linkedlist"
        
        indexcount = 0
        curr = self.head
        prev = self.head

        while indexcount < length_LinkedList:
            prev = curr
            curr = curr.next
            indexcount+=1

        newNode.prev = prev
        prev.next = newNode
        newNode.next = curr
        curr.prev = newNode

    def deleteAtFirst(self):
        if self.head == None:
            return "Linked list is empty nothing to delete" 

        curr = self.head
        self.head = curr.next
        curr.next = None

    def deleteAtEnd(self):
        if self.head == None:
            return "Linked list is empty nothing to delete"
        
        curr = self.head
        prev = self.head
        while curr.next!=None:
            prev = curr
            curr = curr.next
        
        prev.next = None
        curr.prev = None
        

    def deleteAtGivenIndex(self, index):
        pass

    def deleteWithGivenData(self, data):
        pass