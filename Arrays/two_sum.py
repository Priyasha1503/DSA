class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #o(n^2) comp - Bruteforce
        '''for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j'''
        #in o(n) time comp
        #so,now we try to find i,j using the subsratction rather than addition
        '''vis=dict()
        for i in range(0,len(nums)):
            if  target-nums[i] in nums:
                x=nums.index(target-nums[i])
                if x!=i:
                    return i,x'''

            ##this is still more than o(n) that is o(n^2)..so,for that w store the inde values in dict
        ### OPTIMAL APPRAOCH ###
        vis=dict()
        for i in range(0,len(nums)):
            if target-nums[i] in vis:
                return i,vis[target-nums[i]]
            else:
                vis[nums[i]]=i
        print(vis)
