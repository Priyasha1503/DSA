
#https://leetcode.com/problems/running-sum-of-1d-array/?envType=problem-list-v2&envId=prefix-sum

class Solution:
    def runningSum(self, nums: List[int]) -> List[int] :
        ###OPTIMAL PREFIX SUM APPRAOCH
        #TIME COMP O(1) and SPACE COMP O(n)
        length=len(nums)
        prefixSum=[0 for x in range(length)]
        print(prefixSum)
        prefixSum[0]=nums[0]
        print(prefixSum)
        for i in range(1,length):
            print(nums[i])
            prefixSum[i]=prefixSum[i-1]+nums[i]


        return prefixSum

