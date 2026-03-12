class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        pro = 1
        answer = []
        zeroCount = 0
        zeroIndex = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
                zeroIndex = i 
            product *= nums[i]
        if zeroCount == 1:
            for n in nums:
                if n == 0:
                    continue
                pro *= n

        for n in nums:
            if n == 0:
                if zeroCount == 1:
                    answer.append(pro)
                else:
                    answer.append(0)

            else:
                answer.append(product // n)
        return answer