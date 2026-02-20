class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myDict = dict()
        for val in nums:
            if val not in myDict:
                myDict[val] = 1
            else:
                myDict[val] += 1
        for value in myDict.values():
            if value > 1:
                return True
        return False