class Solution:
    def splitString(self, s: str) -> bool:
        found = False
        def backtrack(k, prevNum, count):
            nonlocal found

            if found: 
                return

            if k >= len(s):
                if count >= 2:
                    found = True
                    return
                
            for i in range(k, len(s)):
                num = int(s[k:i+1])
                
                if prevNum < 0 or (prevNum > num and prevNum-num == 1):
                    backtrack(i+1, num, count+1)


        backtrack(0, -1, 0)
        return found