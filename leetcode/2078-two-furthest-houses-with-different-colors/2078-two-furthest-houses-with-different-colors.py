class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        first = colors[0]
        last = colors[-1]
        maxCount1 = 0
        count1 = 0
        maxCount2 = 0
        count2 = 0
        for i in range(1, len(colors)):
            count1 += 1
            if colors[i] != first:
                maxCount1 = count1
        for i in range(len(colors)-2, -1, -1):
            count2 += 1
            if colors[i] != last:
                maxCount2 = count2



        return max(maxCount1, maxCount2)