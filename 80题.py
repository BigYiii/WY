#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，
# 同时保持非零元素的相对顺序
nums=[1,0,9,7,0,4,3,0,8,0]
list1=[]
list2=[]
for i in range(0,len(nums)):
    if nums[i]==0:
        list1.append(nums[i])
    else:
        list2.append(nums[i])
nums=list2+list1
print(nums)