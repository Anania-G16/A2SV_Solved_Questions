class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], x[1]))
        n = float("-inf")
        count = 0
        for interval in intervals:
            if n > interval[0]:
                count += 1
                if n > interval[1]:
                    n = interval[1]
            else:
                n = interval[1]
        return count
                
                 


        
                