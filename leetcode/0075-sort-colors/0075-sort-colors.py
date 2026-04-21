class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {0 : 0, 1 : 0, 2 : 0}
        for n in nums:
            freq[n] += 1
        index = 0
        for i in range(3):
           for j in range(freq[i]):
                nums[j + index] = i
           index += freq[i]


