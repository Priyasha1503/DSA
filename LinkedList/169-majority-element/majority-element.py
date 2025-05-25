from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #-can usse count() or collection-counter module
        #-sort?
        #done bruteforce in Java
        '''maxs=0
        c=Counter(nums)
        print(c)
        for i in c:
            if c[i]>maxs:
                maxs=c[i]
                res=i
        return res'''
        #for tha above one time comp is o(n) but space comp is o(n) too
        #so to make it more optimal and efficient in space comp as asked in question - we use oyer -moore Algorithm for o(1) space comp,o(n) time comp.
        cnt=0
        cand=None #cand is nothing but candidate
        for i in nums:
            if cnt==0:
                cand=i
            if i==cand:
                cnt=cnt+1
            else:
                cnt=cnt-1
        return cand

###In real-world problems (or interviews), if the majority isn't guaranteed, you can add a second pass like this:
'''if nums.count(cand) > len(nums) // 2:
    return cand
else:
    return -1  # or raise error, depending on context'''




            
