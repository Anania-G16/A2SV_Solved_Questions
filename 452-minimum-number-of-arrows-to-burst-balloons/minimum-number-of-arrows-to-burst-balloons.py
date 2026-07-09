class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:( x[1]))
        currentMax = points[0][1]
        arrows = 1
        for scope in points:
            if currentMax >= scope[0]:
                continue
            else:
                arrows += 1
                currentMax = scope[1]
        return arrows
