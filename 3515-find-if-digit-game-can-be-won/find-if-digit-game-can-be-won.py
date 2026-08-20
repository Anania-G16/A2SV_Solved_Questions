class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleSum = 0
        doubleSum = 0
        for n in nums:
            if n < 10:
                singleSum += n
            else:
                doubleSum += n
        if singleSum == doubleSum:
            return False
        return True
