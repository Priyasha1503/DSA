###OPTIMAL SOLUTION ###

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        #Finding middle point
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        #to compare,we need to reverse the second half of the LL...so,reverse LL
        def reverse(node): #nodehre is the strating point of LL
            if node is None:
                return None
            curr=node
            prev=None
            while curr:
                nextnode=curr.next
                curr.next=prev
                prev=curr
                curr=nextnode
            return prev
        rev=reverse(slow.next)
        #comparirng the elements
        #slow=slow.next
        curr1=head
        while curr1 and rev:
            if curr1.val==rev.val:
                curr1=curr1.next
                rev=rev.next
            else:
                return False
        return True
            

