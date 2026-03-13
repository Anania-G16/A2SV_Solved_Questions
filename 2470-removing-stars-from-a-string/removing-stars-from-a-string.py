class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        result = ""
        for ch in s:
            if ch == "*":
                del(stack[-1])
                continue
            stack.append(ch)
        for ch in stack:
            result += ch
        return result