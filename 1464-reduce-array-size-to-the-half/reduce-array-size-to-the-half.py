class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        count = 0
        size = 0
        array = list(freq.items())
        array.sort(key = lambda x: x[1], reverse = True)
        for value, frequency in array:
            size += frequency
            count += 1
            if size >= len(arr) // 2:
                return count
        return 0
