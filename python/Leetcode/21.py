""" Merger two sorted linked list """
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # newNode = None

        if list1 and list2:
            if list1.val <= list2.val:
                newNode = ListNode(list1.val, list1)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val, list2)
                list2 = list2.next
        elif list1 and not list2:
            newNode = list1
            return newNode
        elif list2 and not list1:
            newNode = list2
            return newNode
        else:
            return list1

        firstnode = newNode

        while list1 and list2:
            if list1.val <= list2.val:
                    newNode.next = list1
                    list1 = list1.next
            else:
                newNode.next = list2
                list2 = list2.next

            newNode = newNode.next

        if list1:
            newNode.next = list1
        else:
            newNode.next = list2

        return firstnode

        # if list1 and list2:
        #     if list1.val <= list2.val:
        #         newNode = ListNode(list1.val, list1)
        #         list1 = list1.next
        #     else:
        #         newNode = ListNode(list2.val, list2)
        #         list2 = list2.next
        # elif list1 and not list2:
        #     newNode = list1
        #     return newNode
        # elif list2 and not list1:
        #     newNode = list2
        #     return newNode
        # else:
        #     return list1

        # firstnode = newNode


        # while list1 or list2:
        #     if list1 and list2:
        #         if list1.val <= list2.val:
        #             newNode.next = list1
        #             list1 = list1.next
        #         else:
        #             newNode.next = list2
        #             list2 = list2.next
        #     elif list1 and not list2:
        #         # while list1:
        #         newNode.next = list1
        #         list1 = list1.next
        #     elif list2 and not list1:
        #         # while list2:
        #         newNode.next = list2
        #         list2 = list2.next
        #     else:
        #         break
            
        #     newNode = newNode.next
        
        # return firstnode
        
