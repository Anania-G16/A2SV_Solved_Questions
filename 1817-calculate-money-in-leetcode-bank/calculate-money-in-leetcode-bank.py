class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday = 1
        current = 1

        for day in range(n):
            total += current
            current += 1

            if (day + 1) % 7 == 0:
                monday += 1
                current = monday

        return total