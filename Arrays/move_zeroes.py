


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''z=0
        i=0
        z_bool=False

        while i<len(nums):                                     #SOEMTHING I TRIED....BUT DIDNT GET THE RESULT
            if nums[i]==0:
                z=i
                z_bool=True
                i+=1
            else:
                if z_bool:
                    nums[z],nums[i]=nums[i],nums[z]
                    z+=1
                '''


        z=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[z],nums[i]=nums[i],nums[z]
                z+=1
