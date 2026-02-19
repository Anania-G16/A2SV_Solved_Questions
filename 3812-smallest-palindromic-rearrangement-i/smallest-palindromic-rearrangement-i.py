class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        letters=[]
        for ch in s:                   
            letters.append(ch)

        sorted_letters = sorted(letters)    
        n = len(letters)
        arr = sorted_letters.copy()        
        seen = False
        done = False
        spot = 0
        for ch in sorted_letters:
            if freq[ch] > 1:
                if not seen:
                    arr[spot] = ch
                    next = n-1-spot
                    seen = not seen
                else:                                                                                         
                    spot += 1                        
                    arr[next] = ch                                              
                    seen = not seen
                    freq[ch] -= 2
            else:
                arr[n//2] = ch
                
        result = ""
        for ch in arr:
            result += ch
        return result
                



            