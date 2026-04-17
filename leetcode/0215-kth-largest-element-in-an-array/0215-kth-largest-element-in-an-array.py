class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        count = 0
        
        return nums[k-1]

        

