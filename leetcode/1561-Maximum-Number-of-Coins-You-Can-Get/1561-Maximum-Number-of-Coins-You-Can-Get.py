class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        rem = len(piles)
        added = 0
        result = 0
        piles.sort()
        while added != rem:
            result += piles[rem-2]
            added += 1
            rem -= 2
        return result