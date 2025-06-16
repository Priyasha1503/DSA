#https://leetcode.com/problems/combination-sum/submissions/1666254905/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        

        res=[]
        def helper(ind,target,arr,candidates,n):
            if target<0:
                return
            if ind==n:
                if target==0:
    
                    res.append(arr[:])
                    return
                else:
                    return
            if candidates[ind]<=target:
                arr.append(candidates[ind])
                helper(ind,target-candidates[ind],arr,candidates,n)
                arr.pop()
            helper(ind+1,target,arr,candidates,n)
        
        helper(0,target,[],candidates,len(candidates))
        print(res)
        return res



