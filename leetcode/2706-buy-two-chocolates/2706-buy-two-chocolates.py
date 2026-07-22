class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        original = money
        money -= prices[0] + prices[1]
        return original if money < 0 else money