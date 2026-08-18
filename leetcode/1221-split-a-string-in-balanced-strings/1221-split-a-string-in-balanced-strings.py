class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lCount = 0
        rCount = 0
        result = 0
        for ch in s:
            if ch == 'R':
                rCount += 1
            else:
                lCount += 1
            if rCount == lCount:
                result += 1
                rCount = 0
                lCount = 0
        return result