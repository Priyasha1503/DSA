### next greater element
nums=list(map(int,input().split()))
res=[]
for i in range(0,len(nums)):
    target=nums[i]
    flag=0
    for j in range(i+1,len(nums)):
        if nums[j]>target:
            flag=1
            res.append(nums[j])
            break
    if flag==0:
        res.append(-1)
print(res)
