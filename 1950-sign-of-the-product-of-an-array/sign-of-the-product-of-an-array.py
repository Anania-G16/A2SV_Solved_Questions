class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for n in nums:
            product *= n
        def signFunc(x):
            if x < 0:
                return -1
            elif x > 0:
                return 1
            else:
                return 0
        return signFunc(product)
        