"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        hash = {}
        while temp:
            copy = Node(temp.val)
            hash[copy] = copy
            temp = temp.next

        temp = head

        newNode = Node(0, None)
        while temp:
            newNode.next = hash[temp]
            randomvalue = temp.random
            newNode.random = 

            newNode = newNode.next
            









        """
        Wribg Solution
        newList = Node(0, None, None)
        firstnode = newList
        i = 0
        while head:
            
            temp = Node(head.val, head, head.random)

            node = "node" + str(i)
            node = temp

            newList.next = temp
            newList.random = "node" + str(head.random)
            newList = temp
            head = head.next
        
        return firstnode.next
        """