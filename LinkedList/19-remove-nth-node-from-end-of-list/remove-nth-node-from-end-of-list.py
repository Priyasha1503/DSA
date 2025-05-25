# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''#reversing the list
        prev=None
        curr=head
        nextnode=curr.next
        while curr:
            curr.next=prev
            prev=curr
            curr=nextnode'''
        if head is None:
            return None
        if head.next is None:
            return None
        #creating a dummy node
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy
        for _ in range(0,n):
            curr=curr.next
        fast=curr
        slow=dummy
        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        #deleting the node
        slow.next=slow.next.next
        return dummy.next

        
        



            


