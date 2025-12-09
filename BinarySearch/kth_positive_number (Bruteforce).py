
#https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        #Bruteforce
        maxs=arr[-1]
        sets=set(arr)
        lst=[]
        cnt=0
        for i in range(0,maxs+k+1):
            if i not in sets:
                if cnt==k:
                    return i
                cnt+=1
        return arr[-1]+k
        
            

        
