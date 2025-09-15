#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Optimal appraoch of timecomp o(n2) and space comp o(1)
        result=[]
        nums.sort() #comp o(nlogn)
        for i in range(0,len(nums)):
            #to avoid duplicates
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1

            while j<k:
                total_sum=nums[i]+nums[j]+nums[k]
                if total_sum<0:
                    j+=1
                elif total_sum>0:
                    k-=1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return result

