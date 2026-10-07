class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        n = num

        while n:
            mask = (mask << 1) | 1
            n >>= 1

        return num ^ mask