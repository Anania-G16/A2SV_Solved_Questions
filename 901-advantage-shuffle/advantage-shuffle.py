class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array = list(enumerate(nums2))
        array.sort(key = lambda x : x[1])
        building = []
        nums1.sort()
        result = [0]*len(nums1)
        v = len(nums1)-1
        i = 0
        j = 0

        while i < len(nums1):
            if nums1[i] > array[j][1]:
                building.append((array[j][0], nums1[i]))
                i += 1
                j += 1
            else:
                building.append((array[v][0], nums1[i]))
                v -= 1
                i += 1
        for index, value in building:
            result[index] = value
        return result
