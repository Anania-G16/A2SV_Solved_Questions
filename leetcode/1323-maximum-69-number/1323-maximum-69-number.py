class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        numList = list(s)
        for i in range(len(numList)):
            if numList[i] == '6':
                numList[i] = '9'
                break
        s = "".join(numList)
        s = int(s)
        return s