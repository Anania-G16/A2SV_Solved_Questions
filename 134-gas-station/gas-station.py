class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        starter = 0
        tank = 0
        total = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                starter = i+1
        if total < 0:
            return -1
        return starter        