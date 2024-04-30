"""
    Define here Node class for making Node
"""

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


class CircularLinkedList:

    def insertAtFirst(self, data):
        pass

    def insertAtEnd(self, data):
        pass

    def insertAtMiddle(self, data):
        pass

    def deleteAtFirst():
        pass

    def deleteAtEnd():
        pass

    def deleteAtGivenIndex(self, index):
        pass

    def deleteAtGivenData(self, data):
        pass