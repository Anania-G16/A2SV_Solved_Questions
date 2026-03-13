class Solution:
    def canJump(self, nums: List[int]) -> bool:
       farthest = 0
       current = 0
       while current<len(nums):
        if current > farthest:
            return False
        farthest = max(farthest, current + nums[current])
        current += 1
       return True


        