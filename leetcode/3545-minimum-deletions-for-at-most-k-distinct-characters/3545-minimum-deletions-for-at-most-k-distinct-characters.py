class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = Counter(s)
        arr = list(freq.items())
        arr.sort(key = lambda x: x[1])
        diff = len(arr) - k
        result = 0
        if diff <= 0:
            return 0
        
        for i in range (diff):
            result += arr[i][1]
        return result