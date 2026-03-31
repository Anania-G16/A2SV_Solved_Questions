class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        ans = 0
        while low <= high:
            mid = (high+low) // 2
            if mid * mid <= x:
                ans = mid
                low = mid+1
            else:
                high = mid-1
           
            
        return ans