from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = None
        curr  = head
        initialnode = head
        count = 0
        i = 0

        getlength = 0
        while curr:
            getlength+=1
            curr = curr.next

        nodecount = 0

        prevnodeflag = 0

        curr = head
        while curr:

            if getlength - nodecount >=k:
                if count == 0:
                    firstnode = curr

                next = curr.next
                curr.next = prev
                prev =  curr
                curr = next
                count+=1

                if count == k:
                    firstnode.next = curr
                    if i == 0:
                        initialnode = prev
                        i+=1
                    prev = None
                    count = 0

                    if prevnodeflag == 0:
                        previousnode = firstnode
                    else:
                        previousnode.next = prev
                        previousnode = firstnode
                    
                    prevnodeflag+=1
            else:
                curr = curr.next

            nodecount+=1
        
        return initialnode