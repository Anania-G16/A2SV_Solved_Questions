class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0

        for i in range(n):
            count = ((i + 1) * (n - i) + 1) // 2
            result += arr[i] * count

        return result