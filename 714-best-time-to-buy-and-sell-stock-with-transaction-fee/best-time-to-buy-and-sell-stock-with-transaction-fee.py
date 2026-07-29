class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = float('inf')
        profit = 0
        for price in prices:
            if price < buy:
                buy = price
            else:
                cost = buy + fee
                if price > cost:
                    profit += price - cost
                    buy = price - fee
        return profit