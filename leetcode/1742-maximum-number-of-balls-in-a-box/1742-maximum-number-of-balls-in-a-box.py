class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = Counter()

        for ball in range(lowLimit, highLimit + 1):
            box = sum(int(digit) for digit in str(ball))
            boxes[box] += 1

        return max(boxes.values())