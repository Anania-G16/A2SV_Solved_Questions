class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
     result = []
     i = 0
     while i < len(nums):
        x = nums[i]
        if nums[i] != i+1:
            if nums[i] == nums[x-1]:
                i += 1
            else:
                nums[i], nums[x-1] = nums[x-1], nums[i] 
        else:
            i += 1
     for i in range(len(nums)):
        if nums[i] != i+1:
            result.append(nums[i])
            result.append(i+1)
            break
     return result