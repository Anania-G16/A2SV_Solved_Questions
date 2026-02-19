class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            count = 0
            for i in range(len(nums)):
                if nums[i] < n:
                    count += 1
            result.append(count)
        return result