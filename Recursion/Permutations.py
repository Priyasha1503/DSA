#https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums==[]:return []
        res=[]
        def perm(ind,arr,nums,n,used):
            if len(arr)==n:
                res.append(arr[:])
                return 
            for i in range(0,len(nums)):
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                if used[i]: continue
                used[i]=True
                arr.append(nums[i])
                perm(i+1,arr,nums,n,used)
                arr.pop()
                #perm(i+1,arr,nums,n,used)
                used[i]=False
        used=[False]*len(nums)
        perm(0,[],nums,len(nums),used)
        return res

