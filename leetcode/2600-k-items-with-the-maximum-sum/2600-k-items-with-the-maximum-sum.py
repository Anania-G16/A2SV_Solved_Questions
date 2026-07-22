class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        maxSum = 0
        count = 0
        while numOnes > 0:
            if count == k:
                return maxSum
            maxSum += 1
            count += 1
            numOnes -= 1

        while numZeros > 0:
            if count == k:
                return maxSum
            count += 1
            numZeros -= 1

        while numNegOnes > 0:
            if count == k:
                return maxSum
            maxSum -= 1
            count += 1
            numNegOnes -= 1
        return maxSum

        