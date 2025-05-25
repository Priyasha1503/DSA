# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''#reversing the list and then deleting node and then reversing agin to the normal position to return..becauuse we hae t return head or dummy in specific here..but not returning prev - and ths ttakes 3 passes althugh it is o(n) time comp and o(1)  space comp
        #brute force way - Is to count the number of nodes in a loop without count variable and then delting the node of totalnumber - n nodes given.. '''
        ### OPTIMAL APPROACH ###
        
        if head is None:
            return None
        if head.next is None:
            return None
        #creating a dummy node
        dummy=ListNode(5)
        dummy.next=head
        curr=dummy
        #intilialiisng fast and slow to dummy
        fast=dummy
        slow=dummy
        for _ in range(0,n):
            curr=curr.next
        fast=curr
        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        #deleting the node
        slow.next=slow.next.next
        #we should return dummy.next rther than hea because of edge cases like
        #1.if head is the element tht needs to be deleted
        #2.if there is no


        ## We should return dummy.next instead of head because:
# 1. If the head itself needs to be deleted, dummy.next will now point to the new head.
# 2. It handles edge cases uniformly without extra conditions.

        return dummy.next

        
        



            


