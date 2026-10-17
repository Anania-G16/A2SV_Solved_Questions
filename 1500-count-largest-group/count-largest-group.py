class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}

        for num in range(1, n + 1):
            digit_sum = sum(int(digit) for digit in str(num))
            groups[digit_sum] = groups.get(digit_sum, 0) + 1

        largest = max(groups.values())

        return sum(size == largest for size in groups.values())