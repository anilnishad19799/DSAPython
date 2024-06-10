""" Add two linked list number and return list head"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # if not l1 and not l2:
        #     return l1

        # list1 = []
        # list2 = []

        # while l1:
        #     list1.append(l1.val)
        #     l1 = l1.next
        
        # while l2:
        #     list2.append(l2.val)
        #     l2 = l2.next
        
        # if list1:
        #     list1 = int((''.join(map(str, list1)))[::-1])
        # else:
        #     list1 = 0

        # if list2:
        #     list2 = int((''.join(map(str, list2)))[::-1])
        # else:
        #     list2 = 0

        # output = list1+list2

        # output = str(output)[::-1]
        # output = [int(s) for s in output]

        # newNode = ListNode(output[0])
        # firstnode = newNode
        # for i in range(1, len(output)):
        #     temp = ListNode(output[i])
        #     newNode.next = temp
        #     newNode = temp
        
        # return firstnode

        if not l1 and not l2:
            return l1
        
        newNode = ListNode()
        firstnodeflag = True

        carry = 0

        while l1 or l2:
            sum = 0
            if l1:
                sum+=l1.val
                l1 = l1.next
            
            if l2:
                sum+=l2.val
                l2 = l2.next
            
            sum = sum+carry
            carry = sum // 10
            sum = sum % 10

            temp = ListNode(sum)
            newNode.next = temp
            newNode = temp

            if firstnodeflag:
                firstnode = newNode
                firstnodeflag = False
        
        if carry:
            temp = ListNode(carry)
            newNode.next = temp
            newNode = temp
            
        return firstnode



