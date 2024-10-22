class Solution(object):
    def searchInsert(self, nums, tr):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0,len(nums)
        if tr >nums[high-1] :return high
        if tr <nums[low] :return low

        for _ in nums:
            mid = (low+high)//2
            
            if tr == nums[mid]: return mid
            elif tr>nums[mid]: low = mid+1
            else: high = mid-1
        return  (mid+1)
            
        
        