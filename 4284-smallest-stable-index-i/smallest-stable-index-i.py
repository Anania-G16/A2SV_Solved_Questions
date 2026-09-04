class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        array = []
        maxNum = float('-inf')
        minNum = float('inf')
        for n in nums:
            if n > maxNum:
                maxNum = n
            array.append(maxNum)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < minNum:
                minNum = nums[i]
            array[i] -= minNum

        
        for i in range(len(array)):
            if array[i] <= k:
                return i
        return -1
