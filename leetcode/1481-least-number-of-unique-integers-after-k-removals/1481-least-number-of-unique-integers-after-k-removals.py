class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        array = list(freq.items())
        array.sort(key = lambda x: x[1])
        j = 0
        for pair in array:
            if pair[1] <= k:
                del freq[pair[0]]
                k -= pair[1]
            else:
                return len(freq)
            
        return len(freq)