class Solution:
    def partitionLabels(self, s: str) -> List[int]:
       last = dict()
       result = []
       for i in range(len(s)):
            last[s[i]] = i
       start = 0
       end = -1
       for i in range(len(s)):
            end = max(end, last[s[i]])
            if end == i:
                result.append(end-start+1)
                start = i + 1 
       return result 


    