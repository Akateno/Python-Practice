# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
nums = [0,1,0,3,12]

def move_zeros(nums):
    index=0

    for n in range(len(nums)):
        print(index,n)
        if nums[n]:
            nums[index], nums[n] = nums[n], nums[index]
            index+=1
    return nums 

move_zeros(nums)
 