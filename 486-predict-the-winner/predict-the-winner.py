class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        memo = [[None] * n for _ in range(n)]

        def dp(l, r):
            if l == r:
                return nums[l]

            if memo[l][r] is not None:
                return memo[l][r]

            left = nums[l] - dp(l + 1, r)
            right = nums[r] - dp(l, r - 1)

            memo[l][r] = max(left, right)
            return memo[l][r]

        return dp(0, n - 1) >= 0