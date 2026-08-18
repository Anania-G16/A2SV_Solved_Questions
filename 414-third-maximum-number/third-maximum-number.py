class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = float('-inf')
        sl = float('-inf')
        tl = float('-inf')
        for n in nums:
            if n == l or n == sl or n == tl:
                continue
            if n > l:
                tl = sl
                sl = l
                l = n
                continue
            elif n > sl:
                tl = sl
                sl = n
                continue
            elif n > tl:
                tl = n

        if tl == float('-inf'):
            return l
        return tl