class Solution:
    def minimumPushes(self, word: str) -> int:
        q = len(word) // 8
        rem = len(word) % 8
        x = 1
        result = 0
        while x <= q:
            result += 8*x
            x += 1
        result += rem * x
        return result 