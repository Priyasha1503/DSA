class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def helper(ind,target,ds,candidates,n):
            if target==0:
                res.append(ds[:])
                print(ds)
                return
            else:

                for i in range(ind,n):
                    if target<candidates[i]:
                        break
                    if i>ind and candidates[i]==candidates[i-1]:
                        continue
                    ds.append(candidates[i])
                    helper(i+1,target-candidates[i],ds,candidates,n)
                    ds.pop()


        helper(0,target,[],candidates,len(candidates))
        return res