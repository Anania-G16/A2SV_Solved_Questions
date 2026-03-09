class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
       xy = 0
       yx = 0
       s = s1 + s2
       freq = Counter(s)
    
       for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                xy += 1
            if s1[i] == 'y' and s2[i] == 'x':
                yx += 1
       if (xy + yx) % 2 != 0:
        return -1 
       answer = int(ceil(xy/2)) + int(ceil(yx/2))
       return answer
        
            