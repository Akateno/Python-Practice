# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

nums = [2,14,18,22,22]

def leet(nums):


    hashset=set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
        
    return False
   

leet(nums) 





# nums.sort()
    # print(nums)
    # for i in range(1,len(nums)):
        
    #     if nums[i]!=nums[i-1]:
            
    #         return False
    #     else:
    #         return True