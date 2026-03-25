class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        myMap = dict()
        i = 0
        maxCount = 0
        while i < len(citations):
            if citations[i] not in myMap:
                myMap[citations[i]] = len(citations)-i
            i += 1
        for key, value in myMap.items():
            maxCount = max(maxCount, min(key, value))
        return maxCount
        
        