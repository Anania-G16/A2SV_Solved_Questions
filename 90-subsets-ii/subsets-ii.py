class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        path = []
        nums.sort()
        def backtrack(arr):
            if len(arr) == 0:
                return

            for i in range(len(arr)):
                if i > 0:
                    if arr[i] == arr[i-1]:
                        continue
                path.append(arr[i])
                result.append(path[:])

                candidates = arr[i+1 : ]
                backtrack(candidates)

                path.pop()

        backtrack(nums)
        return result