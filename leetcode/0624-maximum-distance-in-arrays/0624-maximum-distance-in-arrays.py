class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxDistance = float("-inf")
        globalMin = arrays[0][0]
        globalMax = arrays[0][-1]
        for i in range(1, len(arrays)):

            x =abs(globalMax - arrays[i][0])
            maxDistance = max(maxDistance, x)

            x = abs(arrays[i][-1] - globalMin)
            maxDistance = max(maxDistance, x)
            
            globalMax = max(globalMax, arrays[i][-1])
            globalMin = min(globalMin, arrays[i][0])

        return maxDistance
