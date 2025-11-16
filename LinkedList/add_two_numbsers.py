# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1,str2="",""

        while l1 is not None:
            str1=str1+str(l1.val)
            l1=l1.next
        
        while l2 is not None:
            str2=str2+str(l2.val)
            l2=l2.next
        
        num1=int(str1[::-1])
        num2=int(str2[::-1])
        sums=num1+num2
        sums=str(sums)
        sums=sums[::-1]
        dummy=ListNode()
        curr=dummy
        x=0 #for index of sums
        while curr and x<len(sums):
            curr.next=ListNode(int(sums[x]))
            curr=curr.next
            x+=1

        return dummy.next




#more better 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''class Solution:
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
        return dummy.next '''




            
        

