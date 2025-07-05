
#https://leetcode.com/problems/intersection-of-two-linked-lists/?envType=problem-list-v2&envId=hash-table

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #BRUTEFORCE...I guess..
        if headA is None and headB is None:
            return 0
        '''if headA is None and headB is not None:
            return 0'''
        vis=set()
        temp1,temp2=headA,headB
        while temp1:
            vis.add(temp1)
            temp1=temp1.next
        while temp2:
            if temp2 in vis:
                return temp2
            else:
                temp2=temp2.next
        
        
