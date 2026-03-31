class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_pos():
            low, high = 0, len(nums)-1
            ans = -1 
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    high = mid-1
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1       
            return ans
        
        def last_pos():
            low, high = 0, len(nums)-1
            ans = -1 
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    low = mid+1
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1       
            return ans
        first = first_pos()
        last = last_pos()
        return [first, last]
        
