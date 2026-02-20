class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for val in nums1:
            if val in nums2:
                if val not in result:
                    result.append(val)
        return result