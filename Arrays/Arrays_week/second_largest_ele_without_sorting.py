#https://takeuforward.org/plus/dsa/problems/second-largest-element

class Solution:
    def secondLargestElement(self, nums):
        maxs=-1
        sec_maxs=-1
        for i in range(0,len(nums)):
            if nums[i]>maxs:
                sec_maxs=maxs
                maxs=nums[i]
            elif nums[i]<maxs and nums[i]>sec_maxs:
                sec_maxs=nums[i]
        return sec_maxs
