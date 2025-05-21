class Solution:
    def missingNumber(self, nums: List[int]) -> int:


            maxs=max(nums)
            for i in range(0,maxs+1):
                if i not in nums:
                    return i
            return i+1
        