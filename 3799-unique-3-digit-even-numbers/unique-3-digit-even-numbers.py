class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10

        for digit in digits:
            count[digit] += 1

        result = 0

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            used = [0] * 10
            used[a] += 1
            used[b] += 1
            used[c] += 1

            if all(used[d] <= count[d] for d in range(10)):
                result += 1

        return result