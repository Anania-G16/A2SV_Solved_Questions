class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0]*k
        result = float('inf')
        def backtrack(index):
            nonlocal result
            if max(distribution) > result:
                return

            if index >= len(cookies):
                result = min(max(distribution), result)
                return
            
            
            for i in range(k):
                distribution[i] += cookies[index]
              
                backtrack(index+1)

                distribution[i] -= cookies[index]

        backtrack(0)
        return result