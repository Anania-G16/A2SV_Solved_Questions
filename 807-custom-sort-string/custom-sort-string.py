class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        result =  ""
        for ch in order:
            if ch in freq:
                result += ch * freq[ch]
                del(freq[ch])
        for key in freq.keys():
            result += key*freq[key]
        return result