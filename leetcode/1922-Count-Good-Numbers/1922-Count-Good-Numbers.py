class Solution:
    def myPower(self, n: int) -> int:
            result = 1
            MOD = 10 ** 9 + 7
            if n == 1:
                return 20
            else:
                if n % 2 == 0:
                    half = self.myPower(n//2)
                    result = (half * half) % MOD
                else:
                    n -= 1
                    half = self.myPower(n//2)
                    result = (20 * half * half) % MOD 
            return result

    def countGoodNumbers(self, n: int) -> int:
        result = 1
        if n == 1:
            return 5

        if n % 2 != 0:
            result *= 5
            n -= 1

        return (result * self.myPower(n // 2)) % (10 ** 9 + 7)