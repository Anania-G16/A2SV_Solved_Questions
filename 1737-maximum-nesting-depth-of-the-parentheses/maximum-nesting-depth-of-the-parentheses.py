class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxDepth = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
                maxDepth = max(maxDepth, len(stack))
            elif ch == ')':
                stack.pop()
        return maxDepth
                