class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        n = len(arr)
        k = n // 20
        
        trimmed_arr = arr[k : n - k]
        return sum(trimmed_arr) / len(trimmed_arr)