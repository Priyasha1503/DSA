#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2="",""
        dummy=ListNode()
        temp1,temp2=l1,l2
        while temp1!=None:
            num1=num1+str(temp1.val)
            temp1=temp1.next
        while temp2!=None:
            num2=num2+str(temp2.val)
            temp2=temp2.next
        sums=str(int(num1[::-1])+int(num2[::-1]))
        print(sums)
        ind=len(sums)-1
        temp3=dummy
        while ind>=0:
            temp3.next=ListNode(int(sums[ind]))
            temp3=temp3.next
            ind-=1
        return dummy.next




            
        
