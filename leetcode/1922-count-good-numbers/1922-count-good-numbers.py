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
        


        # result = 1
        # if n == 1:
        #     return 5
        # if n == 2:
        #     return 20
        
        # else:
        #     if n % 2 == 0:
        #         if n // 2 != 0:
        #             result = 20 * self.countGoodNumbers(n - 2)
        #         else:
        #             result = self.countGoodNumbers(n // 2) ** 2
        #     else:
        #         n -= 1
        #         result *= 5 * self.countGoodNumbers(n)
                
        # return result % (10 ** 9 + 7)
        
        
        
        # result = 1
        # i = 0
        # while i < n:
        #     if i%2 == 0:
        #         result *= 5
        #     else:
        #         result *= 4
        #     i += 1
        # return result % (10 ** 9 + 7)
        