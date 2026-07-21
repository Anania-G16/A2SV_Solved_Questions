class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        start = 0
        negativeCount = 0
        firstNegative = -1
        lastNegative = -1
        maxCount = 0
        nums.append(0)

        for i in range(len(nums)):
            if nums[i] == 0:
                length = i - start
                end = i - 1
                if negativeCount % 2 == 0:
                    maxCount = max(length, maxCount)
                else:
                    maxCount = max(maxCount, end - firstNegative, lastNegative - start)

                start = i+1
                negativeCount = 0
                firstNegative = -1
                lastNegative = -1

            elif nums[i] < 0:
                if firstNegative == -1:
                    firstNegative = i
                lastNegative = i
                negativeCount += 1
            
        return maxCount