class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        freq = Counter(nums)
        result = 0
        for key in freq.keys():
            if freq[key] == 1:
                result += key
        return result