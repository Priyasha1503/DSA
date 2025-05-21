class Solution:
    def largestElement(self, nums):
        maxs=0
        for i in range(0,len(nums)):
            if nums[i]>maxs:
                maxs=nums[i]
        return maxs
