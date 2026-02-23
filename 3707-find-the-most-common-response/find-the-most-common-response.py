class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        checker = set()
        freq = dict()
        result = []
        largest = 0
        for pack in responses:         
            checker.clear()
            for answer in pack:
                if answer not in checker:
                    checker.add(answer)
                    if answer not in freq:
                        freq[answer] = 1
                    else:
                        freq[answer] += 1
        for key in freq.keys():                     
            if freq[key] > largest:
                result.clear()
                result.append(key)
                largest = freq[key]
            elif freq[key] == largest:
                result.append(key)
            else:
                continue
        result.sort()
        return result[0]
