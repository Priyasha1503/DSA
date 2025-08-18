
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        check=1 #since given positive Integer
        print(check)
        for i in range(0,len(nums)):
            if nums[i]<=0:
                pass
            elif nums[i]==nums[i-1] and i>0:
                pass
            elif nums[i]==check:
                #print(nums[i])
                check=check+1
                print(check)
            else:

                return check
        
        return check
            #edited


