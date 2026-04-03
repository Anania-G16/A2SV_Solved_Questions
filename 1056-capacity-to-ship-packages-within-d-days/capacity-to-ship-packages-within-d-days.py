class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            total =1
            current = 0
            for weight in weights:
                if current + weight > capacity:
                    current = weight
                    total += 1
                else:
                    current += weight
            return total <= days
        
        low, high = max(weights), sum(weights)

        while low <= high:
            mid  = (low + high) // 2
            if can_ship(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low