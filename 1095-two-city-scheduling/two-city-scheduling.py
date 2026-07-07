class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        result = 0
        for cost in costs:
            diff.append(cost[1] - cost[0])
            result += cost[0]
        diff.sort()
        for i in range (len(costs) // 2):
            result += diff[i]
        return result
