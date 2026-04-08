class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canBeGiven(n: int) -> bool:
            count = 0
            if n == 0:
                return True
            for pile in candies:
                count += pile // n
            if count >= k:
                return True 
            return False
        
        small, large = 0, max(candies)
        while small <= large:
            mid = (small + large) // 2
            if canBeGiven(mid):
                small = mid+1
            else:
                large = mid-1
        return large      
                