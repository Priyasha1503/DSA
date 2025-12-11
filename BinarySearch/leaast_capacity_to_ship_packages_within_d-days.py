
#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def func(cap): #cap-capacity
            d=0 #days
            sums=0
            for i in range(0,len(weights)):
                if sums+weights[i]<=cap:
                    sums+=weights[i]
                else:
                    d+=1
                    sums=weights[i]
            return d+1

        low=max(weights)
        high=sum(weights)
        ans=0
        while low<=high:
            mid=(low+high)//2
            res=func(mid)
            if res<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans



            

                
