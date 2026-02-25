class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        c = len(nums)-1
        b = c-1
        a = b-1
        sum = 0
        while(a >= 0):
            if nums[a] + nums[b] > nums[c]:
                return nums[a] + nums[b] + nums[c]
            else:
                a -= 1
                b -= 1
                c -= 1
        return sum

