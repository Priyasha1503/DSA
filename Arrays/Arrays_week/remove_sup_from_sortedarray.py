
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x,i=0,0

        while x<len(nums) and i<len(nums):
            if nums[x]==nums[i]:
                i+=1
            else:
                nums[x+1]=nums[i]
                x+=1
                i+=1
        return x+1
