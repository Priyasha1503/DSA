#https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       ###BRUTEFORCE
        '''store=[0,0,0]         # or rather than arrays we coud take cnt1,cnt2,cnt3 for mpre better ompletxies of space..
        length=len(nums)
        res=[]
        print(res)
        for i in nums:
            if i==0:
                store[0]+=1 
            elif i==1:
                store[1]+=1
            else:
                store[2]+=1
        for i in range(0,length): #inserting into res
            if i<store[0]:
                nums[i]=0
            elif i<store[1]+store[0]:
                nums[i]=1
            elif i<store[2]+store[1]+store[0]:
                nums[i]=2
        print(store)'''
        ### optimal
        ##NATIONAL DUTCH FLAG ALGORITHM
        low,mid=0,0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                #replace low,mid
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                #replace mid and high
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums


        
