class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return []
        
        storelist = []
        temp = head
        while temp!=None:
            storelist.append(temp.val)
            temp = temp.next
        
        return storelist[::-1]