class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        path = []
        def subset(arr):
            if len(arr) == 0:
                return
            for n in arr:
                path.append(n)
                result.append(path[:])
                
                index = arr.index(n)
                candidates = arr[index+1 :]
                subset(candidates)

                path.pop()
        subset(nums)
        return result
