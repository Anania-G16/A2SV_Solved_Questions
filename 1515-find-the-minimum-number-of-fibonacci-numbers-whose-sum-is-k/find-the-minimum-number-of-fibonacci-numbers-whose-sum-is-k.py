class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def genFib(k):
            fibArr = []
            n = 0
            left = 0
            right = 1
            while True:
                if n == 0 or n == 1:
                    fibArr.append(1)
                else:
                    x = fibArr[left] + fibArr[right]
                    if x > k:
                        break
                    fibArr.append(x)
                    left += 1
                    right += 1
                n += 1
            return fibArr

        fibArr = genFib(k)
        count = 0
        for i in range(len(fibArr)-1, -1, -1):
            if fibArr[i] <= k:
                k -= fibArr[i]
                count += 1
            if k == 0:
                return count
        return count





            
                





        