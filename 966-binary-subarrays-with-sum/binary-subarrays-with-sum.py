class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        myMap = dict({0 : 1})
        prefix = 0
        result = 0
        for n in nums:
            prefix += n
            x = prefix-goal
            if x in myMap:
                result += myMap[x]
            if prefix not in myMap:
                myMap[prefix] = 1
            else:
                myMap[prefix] += 1
        return result