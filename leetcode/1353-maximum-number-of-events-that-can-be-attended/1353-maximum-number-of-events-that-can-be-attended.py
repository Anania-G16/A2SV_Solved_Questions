class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        heap = []
        day = 1
        result = 0

        i = 0
        events.sort()

        while i < len(events) or heap:
            while i < len(events) and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1
            
            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                result += 1

            day += 1
        
        return result
