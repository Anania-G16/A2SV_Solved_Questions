class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix_sum = []
        sum = 0
        for n in nums:
            sum += n
            prefix_sum.append(sum)
        count = 0
        for i in range(len(nums)-1):
            if (prefix_sum[i] - (prefix_sum[-1] - prefix_sum[i])) % 2 == 0:
                count += 1
        return count
