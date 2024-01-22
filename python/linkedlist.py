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

    ## Insertion Operation
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

        ### Delete Operation 
    
    def deleteAtFirst(self):
        if self.head==None:
            print("No element to delete")
        self.head = self.head.next

    def deleteAtLast(self):
        if self.head == None:
            print("No element is present")
        curr = self.head
        prevnode = self.head
        while curr.next!=None:
            prevnode = curr.next
            curr = curr.next
        prevnode.next = None

    def deleteAtGivenPosition(self, pos):
        if self.head == None:
            print("Empty List")
        totallength = self.getLengthLinkedList()
        if totallength==1:
            self.head = None
        curr = self.head
        prevnode = self.head
        count = 0
        while count<pos-1 or curr.next!=None:
            prevnode = curr
            curr =  curr.next
        prevnode.next = curr.next      


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
