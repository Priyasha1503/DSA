
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)-1): #here we should be using lennums-1 rather than jus len(nums)..for edge cases//although all test cases are executed from the jus len(nums)
            if nums[i]==nums[i+1]:
                return nums[i]
            else:
                pass      

            #time comp -o(nlogn)+o(n)=o(nlogn)
            #but to make it slightly better appraoach..we can use hash set
            #but for optimal appraoch..we should be usiing Tortoise Haire method      
            

        

            



