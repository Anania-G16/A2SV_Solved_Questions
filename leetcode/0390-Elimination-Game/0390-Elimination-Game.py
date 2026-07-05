class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        rem = n
        fromLeft = True

        while rem > 1:
            if fromLeft  or rem % 2 == 1:
                head += step
            step *= 2
            rem //= 2
            fromLeft = not fromLeft

        return head