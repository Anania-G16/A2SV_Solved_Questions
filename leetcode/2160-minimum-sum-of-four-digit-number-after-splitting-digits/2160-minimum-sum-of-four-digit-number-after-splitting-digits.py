class Solution:
    def minimumSum(self, num: int) -> int:
        s = str(num)
        sList = list(s)
        sList.sort()

        numstr1 = sList[0] + sList[2]
        numstr2 = sList[1] + sList[3]

        a = int(numstr1)
        b = int(numstr2)

        return a + b