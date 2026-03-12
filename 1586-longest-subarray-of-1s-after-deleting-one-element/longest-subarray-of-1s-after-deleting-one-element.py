class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        index = -1
        results = []
        while right < len(nums):
            if nums[right] == 1:
                right += 1
            else:
                if index == -1:
                    index = right
                    right += 1
                else:
                    results.append(right - left-1)
                    left = index + 1
                    index = right
                    right += 1
        results.append(right - left-1)
        return max(results)

            

