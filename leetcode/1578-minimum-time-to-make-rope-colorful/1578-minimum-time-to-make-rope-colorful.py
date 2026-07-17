class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        prev = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[prev]:
                if neededTime[i] < neededTime[prev]:
                    time += neededTime[i]
                else:
                    time += neededTime[prev]
                    prev = i
            else:
                prev = i
        return time