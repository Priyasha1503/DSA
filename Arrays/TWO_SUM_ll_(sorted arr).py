
#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=problem-list-v2&envId=binary-search

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        #Using Binary Search
        low=0
        high=len(numbers)-1

        '''while0 low<=high:
            mid=(low+high)//2
            res=abs(target-numbers[low])
            if res==numbers[mid]:
                return [low+1,mid+1]                          ### tHI SI WRONG..JUS KINDA TRIED THIS METHOD
            elif res<=numbers[mid]:
                high=mid-1
            else:
                low=mid+1
        
        return [-1,-1]'''
        while low<=high:
            res=numbers[low]+numbers[high]
            if res==target:
                return [low+1,high+1]
            elif res<target:
                low+=1
            else:
                high-=1
        return [-1,-1]
