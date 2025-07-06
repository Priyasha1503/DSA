class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==1 and nums[0]==val:
            return 0

        if len(nums)==1 and nums[0]!=val:
            return 1

        first,last=0,len(nums)-1
        while first<=last:
            if nums[first]==val and nums[last]!=val:
                nums[first]=nums[last]
                first+=1
                last-=1
            elif nums[first]==val and nums[last]==val:
                last-=1
            else:
                first+=1

        return last+1


##clean and most optimal version iutseems...by chatgpt..
'''class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n '''
