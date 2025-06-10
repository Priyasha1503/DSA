#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sets=set(nums)
        for i in range(0,len(nums)):
            if i not in sets:
                return i

        return i+1
