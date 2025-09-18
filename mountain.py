

#mountain q..longest subarray of numbers sequenicng like a mountain---number increaing ,reaching its peak,an then decreasing
nums=list(map(int,input().split()))
maxs=0
for i in range(0,len(nums)-1):
    total_count=0
    gng_to_peek=i
    nxt_ind=i
    check=0
    while nums[gng_to_peek]<nums[gng_to_peek+1] and gng_to_peek<len(nums)-2:
        #gng to top of the mountain
        check=1
        gng_to_peek+=1
        nxt_ind+=1
        total_count+=1
    if check==1:
        while nums[nxt_ind]>nums[nxt_ind+1] and nxt_ind<len(nums)-2:
            total_count+=1
            nxt_ind+=1
            
        if nums[nxt_ind]>nums[-1]:
            total_count+=1


    maxs=max(total_count+1,maxs)
        
        
    
print(maxs)
