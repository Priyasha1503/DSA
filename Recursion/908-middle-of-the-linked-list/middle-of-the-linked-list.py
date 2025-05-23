# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1=head
        temp2=head
        pos=0
        while temp1.next and temp2.next:
            temp1=temp1.next
            if pos%2==0:
                temp2=temp2.next
            pos=pos+1
        return temp2

##checj=king if the pos  is even ..so that I  could jump temp2 once 
# and with this temp1 will be jumped for every step and this makes temp1 jump for 2steps and temp2 for one step

        