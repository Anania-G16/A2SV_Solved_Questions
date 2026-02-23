class Solution:
    def romanToInt(self, s: str) -> int:
        myDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        myDict2 = {'I': ('V', 'X'), 'X': ('L', 'C'), 'C': ('D', 'M')}
        result = 0
        for i in range(len(s)-1):
            if s[i] in myDict2 and s[i+1] in myDict2[s[i]]:
                result -= myDict[s[i]]
            else:
                result += myDict[s[i]]
        return result + myDict[s[len(s)-1]]

