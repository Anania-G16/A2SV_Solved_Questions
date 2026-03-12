class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        running_sum = 0
        max_sum = float('-inf')

        while i < len(nums):
            running_sum = max(nums[i], running_sum + nums[i])
            i += 1
            max_sum = max(max_sum, running_sum)
        
        return max_sum
