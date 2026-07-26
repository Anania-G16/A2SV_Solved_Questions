class Solution:
    def fillCups(self, amount: List[int]) -> int:
        count = 0
        amount.sort()
        while amount[-1] > 0:
            amount[1] -= 1
            amount[2] -= 1
            count += 1
            amount.sort()
        return count
