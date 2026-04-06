class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mid = float('-inf')
        for current in reversed(nums):
            if current < mid:
                return True
            while stack and current > stack[-1]:
                mid = stack.pop()
            stack.append(current)
        return False


