""" Remove nth node from End of list """

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return head
        

        temp = head
        firstnode = head
        lenlist = 0

        while temp:
            temp = temp.next
            lenlist+=1

        gotonode = lenlist - n 

        if gotonode == 0:
            return head.next

        curr = head

        for i in range(gotonode-1):
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
        
        return firstnode