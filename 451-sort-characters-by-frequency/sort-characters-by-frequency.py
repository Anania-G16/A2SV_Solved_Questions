class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        p = ""
        for key in freq.keys():
            for i in range (freq[key]):
                p += key
        sorted_chars = "".join(sorted(p, key = lambda x:freq[x], reverse = True))
        return sorted_chars
        