
nums = [1,1,2]

def remove_duplicates(nums):
    count=1
    for i in range(1,len(nums)-1):
        if nums[i] != nums[i-1]:
            nums[count]= nums[i]
            count+=1
        




remove_duplicates(nums)
