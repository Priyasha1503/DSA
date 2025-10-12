#https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

class Solution:
    def leaders(self, arr):
        # code here
        
        maxs=-float('inf')
        res=[]
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>=maxs:
                res.append(arr[i])
            maxs=max(maxs,arr[i])
        res=res[::-1]
        return res
