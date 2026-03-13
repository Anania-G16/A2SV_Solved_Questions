class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myMap = dict()
        index = -1
        result = []
        for i in range(len(nums2)):
            myMap[nums2[i]] = i

        for n in nums1:
            index = myMap[n]
            found = False
            while index < len(nums2):
                if nums2[index] > n:
                    found = True
                    result.append(nums2[index])
                    break
                index += 1
            if not found:
                result.append(-1) 
        return result

