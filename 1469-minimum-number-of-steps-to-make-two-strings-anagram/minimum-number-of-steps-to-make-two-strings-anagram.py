class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = dict()
        count = 0 
        for ch in t:
            if ch not in freq:            
                freq[ch] = 1            
            else:                        
                freq[ch] += 1
        for ch in s:
            if ch not in freq:
                count += 1
            else:
                freq[ch] -= 1
                if freq[ch] == 0:
                    del(freq[ch])
        return count
     
        
        