class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        val = 0
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                if stack[-1] == 0:
                    val = 1
                else:
                    val = stack[-1]*2
                stack.pop()
                if not stack:
                    score += val
                else:
                    stack[-1] += val

        return score
