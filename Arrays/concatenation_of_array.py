
#https://leetcode.com/problems/concatenation-of-array/?envType=problem-list-v2&envId=array


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''ans=nums+nums
        return ans'''
        ans=[]
        for i in range(0,len(nums)*2):
            ans.append(nums[i%(len(nums))])
        return ans
