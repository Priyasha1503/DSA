
#https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #one appraoch
        '''sets=set(nums)
        n=len(nums)
        for i in range(0,n):
            if i not in nums:
                return i
        return i+1'''
        #optimal appraoch
        n=len(nums)
        formula=(n*(n+1))//2
        print(formula)
        return abs(sum(nums)-formula)

  ###We can do this using XOR as welll
