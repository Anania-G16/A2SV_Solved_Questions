class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        last = -1
        for i in range(len(nums)):
            if last >= nums[i]:
                diff = last - nums[i]
                count += diff + 1
                last = nums[i] + diff + 1
            else:
                last = nums[i]
        return count