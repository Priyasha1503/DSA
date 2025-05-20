class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            if 0<=nums[i]<=9:
                if i==nums[i]:
                    return i
            else:
                x=str(nums[i])
                sums=0
                for p in range(0,len(x)):
                    sums=sums+int(x[p])
                if i==sums:
                    return i
        return -1
                
                
