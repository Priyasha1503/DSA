#https://leetcode.com/contest/weekly-contest-471/problems/sum-of-elements-with-frequency-divisible-by-k/

from collections import Counter
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        '''#finding out the frequency of each element
        sum=0
        c=Counter(nums)
        for i in c:
            #print(i)
            #print(c[i])
            if c[i]%k==0:
                sum+=(c[i]*i)
        return sum
        '''
        d=dict()
        for i in range(0,len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        print(d)
        sum=0
        for i in d:
            if d[i]%k==0:
                sum+=d[i]*i
        return sum

        
