class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i):
            result = ""
            num = 0
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    temp, i = decode(i+1)
                    result += num * temp
                    num = 0
                elif s[i] == ']':
                    return result, i
                else:
                    result += s[i]
                i += 1
            return result, i
        result, i = decode(0)
        return result