class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = sorted(zip(difficulty, profit), key = lambda x: x[0])
        worker.sort()
        w = 0
        d = 0
        profit = 0
        maxProfit = 0
        broken = False
        while w < len(worker):
            if worker[w] >= arr[d][0]:
                maxProfit = max(maxProfit, arr[d][1])
                if d == len(difficulty) - 1:
                    broken = True
                    break
                d += 1
            else:
                profit += maxProfit
                w += 1
        if broken:
            for i in range(w, len(worker)):
                profit += maxProfit
                
        return profit


