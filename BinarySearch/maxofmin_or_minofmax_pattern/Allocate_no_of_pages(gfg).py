
#https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1


class Solution:
    def findPages(self, arr, k):
        # code here
        
        #base case
        if len(arr)<k:
            return -1
        
        #it checks if for  the value of mid,it can allot the 
        #number of books in less than or euql to the k value
                    

        def func(mid):
            sums=0
            cnt=1
            for i in range(0,len(arr)):
                if arr[i]+sums>mid:
                    sums=arr[i]
                    cnt+=1
                else:
                    sums+=arr[i]
            return cnt
            
        low=max(arr)
        high=sum(arr)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            res=func(mid)
            if res<=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
            
            
