class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        max_heap = []
        result = []

        for key, v in freq.items():
            heapq.heappush(max_heap, (-v, key))

        for i in range(k):
            word = heapq.heappop(max_heap)
            result.append(word[1])
        return result