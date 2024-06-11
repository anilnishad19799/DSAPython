# Definition for singly-linked list.
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        allvalue = []
        for listval in lists:
            startnode = listval

            while startnode:
                allvalue.append(startnode.val)
                startnode = startnode.next

        allvalue = sorted(allvalue)
        
        newNode = ListNode()
        firstNode = newNode

        for i in allvalue:
            temp = ListNode(i)
            newNode.next = temp
            newNode = temp

        return firstNode.next