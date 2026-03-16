class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for ch in logs:
            if ch == "../":
                if len(stack) > 0:
                    stack.pop()
            elif ch == "./":
                continue
            else:
                stack.append(ch)
        return len(stack)