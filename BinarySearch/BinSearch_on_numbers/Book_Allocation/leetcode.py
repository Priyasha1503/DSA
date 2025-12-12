
#https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #optimized - Binsearch

#it checks if for  the value of mid,it can allot the 
        #number of books in less than or euql to the k value
        def func(mid):
            sums=0
            cnt=1
            for i in range(0,len(nums)):
                if sums+nums[i]<=mid:
                    sums+=nums[i]
                else:
                    cnt+=1
                    sums=nums[i]
            return cnt
        low=max(nums)
        high=sum(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            count=func(mid)  #this gives the days/no. of parts it take to allocate the whole array
            if count<=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        
        return ans

