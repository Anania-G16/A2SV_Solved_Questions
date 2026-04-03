class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                return mid
        result = high+1 if target>nums[high] else high
        return 0 if result < 0 else result