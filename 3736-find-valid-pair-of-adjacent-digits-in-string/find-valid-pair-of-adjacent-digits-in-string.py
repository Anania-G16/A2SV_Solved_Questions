class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        result = ""
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                if freq[s[i]] == int(s[i]) and freq[s[i+1]] == int(s[i+1]):
                    result += s[i] + s[i+1]
                    break
        return result
            