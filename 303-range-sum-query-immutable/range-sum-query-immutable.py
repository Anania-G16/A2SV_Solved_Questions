class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        sum = 0
        for n in nums:
            sum += n
            self.prefix_sum.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)