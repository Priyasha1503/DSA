#https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=[]
        for i in nums1:
            lst.append(i)
        for j in nums2:
            lst.append(j)
        lst.sort()

        if len(lst)%2==0:
            mid=int((len(lst)-1)/2)
            r=(lst[mid]+lst[mid+1])/2
            return float(r)
        else:
            mid=int(len(lst)/2)
            r=lst[mid]
            return float(r)
        
