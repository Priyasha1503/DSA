class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0,[],nums,[])
        


    def helper(self,ind,ds,nums,lst):
        if(ind==len(nums)):
            lst.append(ds[:])
            return lst
        else:
            ds.append(nums[ind])
            self.helper(ind+1,ds,nums,lst)
            ds.pop()
            self.helper(ind+1,ds,nums,lst)
            return lst
           


        