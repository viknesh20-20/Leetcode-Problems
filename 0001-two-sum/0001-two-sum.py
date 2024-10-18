class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(len(nums)-1,i,-1):
                if nums[i]+nums[j] == target:
                    return [i,j]
                
       
        
           