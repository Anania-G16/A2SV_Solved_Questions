class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        i = 0
        j = i+1
        count = 0
        while i < len(nums)-1:
            j = i+1
            while j < len(nums):
                if i*j % k == 0:
                    if nums[i] == nums[j]:
                        count += 1
                j += 1
            i += 1
        return count