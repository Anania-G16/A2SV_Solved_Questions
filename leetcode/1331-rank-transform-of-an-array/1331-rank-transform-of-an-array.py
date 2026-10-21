class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_array = sorted(arr)
        myMap = dict()
        rank = 1
        for n in sorted_array:
            if n not in myMap:
                myMap[n] = rank
                rank += 1
        result = []
        for n in arr:
            result.append(myMap[n])
        return result