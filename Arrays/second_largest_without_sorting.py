###find the second smallest and largest element in the list
nums=list(map(int,input().split()))
maxs=0
sec_max=0#second max
#should include the base cases of if n<2
#should include for negative numbers..so,maxs,sec_max= negativefloat('inf'),negativefloat('inf')
for i in range(0,len(nums)):
    if nums[i]>maxs:
        
        sec_max=maxs
        maxs=nums[i]
print(sec_max)

        
