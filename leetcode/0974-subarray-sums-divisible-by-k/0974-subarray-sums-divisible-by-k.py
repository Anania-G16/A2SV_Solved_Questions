class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        myMap = {0:1}
        prefix = 0
        count = 0
        for n in nums:
            prefix += n
            rem = prefix % k
            count += myMap.get(rem, 0)
            myMap[rem] = myMap.get(rem, 0)+1
        return count