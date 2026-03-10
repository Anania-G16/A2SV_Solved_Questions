class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = []
        running_sum = 0
        for n in nums:
            running_sum += n
            prefix.append(running_sum)
        smallest = min(prefix)
        if smallest >= 0:
            return 1
        return abs(smallest) + 1