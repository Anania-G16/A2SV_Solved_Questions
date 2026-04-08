class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def isPossible(d: int) -> bool:
            placed = 0
            lastPlaced = float('-inf')
            for n in position:
                if n - lastPlaced >= d:
                    placed += 1
                    lastPlaced = n
            if placed >= m:
                return True
            return False

        position.sort()
        small, big = 1, position[-1] - position[0]
        while small <= big:
            mid = (small + big) // 2
            if isPossible(mid):
                small = mid + 1
            else:
                big = mid - 1
        return big
