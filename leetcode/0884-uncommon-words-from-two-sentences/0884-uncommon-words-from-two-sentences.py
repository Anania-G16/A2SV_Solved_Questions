class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words = s1.split()
        words2 = s2.split()
        words += words2
        freq = Counter(words)
        result = []
        for key, value in freq.items():
            if value == 1:
                result.append(key)
        return result
