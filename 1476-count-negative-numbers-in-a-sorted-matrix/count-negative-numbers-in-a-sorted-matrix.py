class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for arr in grid:
            for n in arr:
                if n < 0:
                    count += 1
        return count
