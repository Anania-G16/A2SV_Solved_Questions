class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        op1 = True
        for key in freq2.keys():
            if key not in freq1:
                return False
        for key in freq1.keys():
            if key not in freq2:
                return False
            if freq1[key] != freq2[key]:
                op1 = False
                break
        if op1:
            return True
        freqList1 = []
        freqList2 = []
        for value in freq1.values():
            freqList1.append(value)
        for value in freq2.values():
            freqList2.append(value)
        freqList1.sort()
        freqList2.sort()
        return freqList1 == freqList2