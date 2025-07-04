#https://leetcode.com/problems/find-peak-element/?envType=problem-list-v2&envId=array

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums)==0 or len(nums)==1 :
            return 0

        '''if len(nums)==2:
            if nums[0]>nums[1]: return 0
            else : return 1'''
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i]>nums[i+1]:
                return i
        if nums[0]>nums[len(nums)-1]:
            return 0
        if nums[len(nums)-1]>nums[0]:
            return len(nums)-1

        return 0
        
            
        
