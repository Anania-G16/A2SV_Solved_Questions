class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # j = 0
        # result = []
        # while i < len(nums)
        #     x = nums[j]-1
        #     if nums[j] == j+1:
        #         j += 1
        #     else:
        #         if nums[j] == nums[x]:
        #             if nums[j] not in result:
        #                 result.append(nums[j])
        #                 j += 1
        #         else:
        #             nums[j], nums[x] = nums[x], nums[j]
        # return result

        result = []
        for num in nums:
            index = abs(num)-1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] *= -1
        return result