class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        myMap = {0:1}
        prefix = 0
        count = 0
        for n in nums:
            prefix += n
            x = prefix - goal
            if x in myMap:
                count += myMap[x]
            if prefix not in myMap:
                myMap[prefix] = 1
            else:
                myMap[prefix] += 1
        return count
                