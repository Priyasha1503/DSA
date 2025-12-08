
#https://leetcode.com/problems/koko-eating-bananas/

from  math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def reqtime(k):  #required time of k units
            total_hours=0
            for i in range(0,len(piles)):
                #total_hours+=ceil(float(piles[i])/float(k))
                total_hours+=ceil(piles[i]/k)
            return total_hours
        
        #BRUTE FORCE
        '''k=1
        while reqtime(k)>h:
            k+=1
        
        return k'''



        #OPTIMAL

        #the range of k could be from 0 to mmax(piles)
        low=1
        high=max(piles)
        ans=float(inf)
        while low<=high:
            mid=(low+high)//2
            req=reqtime(mid)
            if req<=h: #it is in region    ///// xxxx  ...so, we should eliminate right side
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
                
        
