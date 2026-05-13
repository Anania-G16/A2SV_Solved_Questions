class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for s in stones:
            heapq.heappush(max_heap, -s)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            diff = first-second
            if diff > 0:
                heapq.heappush(max_heap, -diff)

        if max_heap:
            return -heapq.heappop(max_heap)
        return 0


