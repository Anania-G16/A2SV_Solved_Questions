class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n < 0:
            x = 1/x
            n = abs(n)
        if n == 1:
            return x
        if n == 0:
            return 1
        else:
            if n % 2 == 0:
                result *= self.myPow(x, n//2) ** 2
            else:
                n -= 1
                result *= x * self.myPow(x, n//2) ** 2
            
        return result
        