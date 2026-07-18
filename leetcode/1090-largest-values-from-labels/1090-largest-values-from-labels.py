class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        array = list(zip(values, labels))
        array.sort(key = lambda x: x[0], reverse = True)

        count = 0
        result = 0
        used = Counter()

        for pair in array:
            if count == numWanted:
                return result
            
            if used[pair[1]] < useLimit:
                result += pair[0]
                count += 1
                used[pair[1]] += 1

        return result
