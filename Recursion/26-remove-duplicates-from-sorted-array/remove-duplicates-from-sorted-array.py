class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''slow=0
        fast=0
        while(fast<len(nums)):
            if nums[fast]!=nums[slow]:
                nums[slow]=nums[fast]
                slow=slow+1
                fast=fast+1
            else:
                fast=fast+1
        return slow'''
        slow=0
        for fast in range(0,len(nums)):
            if nums[fast]!=nums[slow]:
                slow=slow+1
                nums[slow]=nums[fast]
        return slow+1