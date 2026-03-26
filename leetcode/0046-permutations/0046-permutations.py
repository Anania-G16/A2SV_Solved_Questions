class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(remaining):
            if len(remaining) == 0:
                result.append(path[:])
                return

            for n in remaining:
                path.append(n)

                new_remaining = [x for x in remaining if x != n]
                backtrack(new_remaining)

                path.pop()
        backtrack(nums)
        return result