class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        running_sum = 0
        for n in nums:
            running_sum += n
            result.append(running_sum)
        return result
