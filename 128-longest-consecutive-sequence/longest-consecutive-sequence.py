class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        mySet = set()
        for num in nums:
            if num not in mySet:
                mySet.add(num)
        nums.clear()
        for num in mySet:
            nums.append(num)
        nums.sort()
        right = 0
        sequence = 1
        maxSequence = 1
        while right < len(nums)-1: 
            if nums[right] + 1 == nums[right+1]:
                right += 1
                sequence += 1
            else:
                maxSequence = max(sequence, maxSequence)
                sequence = 1
                right += 1

        return max(sequence, maxSequence)
