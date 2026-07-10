class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        currentMax = nums[-1]
        left = 0
        right = len(nums)-2
        result = 0
        for i in range(len(nums)-1, 1, -1):
            currentMax = nums[i]
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > currentMax:
                    result += right - left
                    right -= 1
                else:
                    left += 1
        return result

