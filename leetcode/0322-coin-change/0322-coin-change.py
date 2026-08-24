class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = deque()
        level = 1
        visited = set()
        for coin in coins:
            queue.append(coin)
        
        while queue:
            size = len(queue)
            for i in range(size):
                running_sum = queue.popleft()
                if running_sum == amount:
                    return level
                for coin in coins:
                    total = running_sum + coin
                    if total not in visited and total <= amount:
                        queue.append(running_sum + coin)
                        visited.add(total)
            level += 1
        return -1
        
