# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        prev=None
        curr=head
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        return prev
        