# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersection_two_arrays(nums1,nums2):
    
    hashset={}
    nums3=[]

    for n in nums1:
       if n in hashset:
           hashset[n]+=1
       else:
           hashset[n]=1
    
        
    for n in nums2:
        if n in hashset and hashset[n]>0:
            nums3.append(n)
            hashset[n]-=1
            print(nums3)
    
        

intersection_two_arrays(nums1,nums2)