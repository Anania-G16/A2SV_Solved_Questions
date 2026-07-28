class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ""
        for i in range(1, n+1):
            if (n-i) * 26 >= k-1:
                result += 'a'
                k -= 1
            else:
                x = k % 26
                if x == 0:
                    result += 'z'
                    k -= 26
                else:
                    result += chr(x+96)
                    k -= x
        return result
