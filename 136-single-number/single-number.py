class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sin = 0
        for i in nums:
            sin ^= i
        return sin