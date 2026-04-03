class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low, high = 0, len(citations)-1
        maxH = 0
        papers = 0
        found = False
        while low <= high:
            mid = (low + high) // 2
            papers = len(citations) - mid
            if citations[mid] <= papers:
                maxH = max(maxH, citations[mid])
                low = mid+1
                found = True
            else:
                maxH = max(maxH, papers)
                high = mid-1
        return maxH
