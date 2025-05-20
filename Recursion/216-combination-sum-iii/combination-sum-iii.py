class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        lstcomp=[x for x in range(1,10)]
        res=[]
        lstcomp.sort()
        def helper(ind,n,arr,lstcomp,length):
            if n==0:
                if len(arr)==k:
                    res.append(arr[:])
                    return
            for i in range(ind,length):
                if n<lstcomp[i]:
                    break
                arr.append(lstcomp[i])
                helper(i+1,n-lstcomp[i],arr,lstcomp,length)
                arr.pop()
            
        helper(0,n,[],lstcomp,len(lstcomp))
        return res