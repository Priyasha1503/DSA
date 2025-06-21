
#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return list2
        if list1 is not None and list2 is None:
            return list1
        if list1 is None and list2 is None:
            return None
        dummy=ListNode()
        curr=dummy
        temp1,temp2=list1,list2
        while temp1 and temp2:
            if temp1.val<temp2.val:
                curr.next=temp1
                temp1=temp1.next
                curr=curr.next
            elif temp2.val<=temp1.val:
                curr.next=temp2
                temp2=temp2.next
                curr=curr.next
        while temp1:
            curr.next=temp1
            temp1=temp1.next
            curr=curr.next
        while temp2:
            curr.next=temp2
            temp2=temp2.next
            curr=curr.next

        return dummy.next
            

