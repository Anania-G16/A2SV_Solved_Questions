class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        freq = Counter(s)
        seen = set()
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                seen.add(s[i])

            elif stack[-1] < s[i]:
                if s[i] not in seen:
                    stack.append(s[i])
                    seen.add(s[i])

            else:
                if s[i] not in seen:
                    while len(stack) > 0 and freq[stack[-1]] > 1 and stack[-1] >= s[i]:
                        ch = stack.pop()
                        seen.discard(ch)
                        freq[ch] -= 1
                    stack.append(s[i])
                    seen.add(s[i])
                else:
                    freq[s[i]] -= 1
        result = "".join(stack)
        return result
