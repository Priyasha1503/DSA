# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        ###we could take the loop and once again the second head comes we will return tru..but here in q , we dont know exactly thelink is taken with head..it can be excluding head too like example 1 beside this
        sets=set()
        temp=head
        while temp:
            if temp in sets:
                return True
            else:
                sets.add(temp)
            temp=temp.next
        return Falsea
    
                    





        
        
