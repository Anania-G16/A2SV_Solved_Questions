class Solution:
    def largestOddNumber(self, num: str) -> str:
        candidate = ""
        result = ""
        for n in num:
            candidate += n
            if int(n) % 2 == 1:
                result = candidate
        return result