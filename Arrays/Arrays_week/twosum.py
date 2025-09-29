
#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: ###revision for OA visa
        #bruteforce
        '''for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]'''
        #optimal
        d=dict()
        for i in range(0,len(nums)):
            d[nums[i]]=i#storing all the array values and its ondex in dict
        for i in range(0,len(nums)):
            if abs(nums[i]-target) in d and i!=d[abs(nums[i]-target)]:
                return [i,d[abs(nums[i]-target)]]
        return -1

