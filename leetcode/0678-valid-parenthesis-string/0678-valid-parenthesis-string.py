class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        p = []
        for i in range(len(s)):
            if s[i] == '(':
                p.append(i)
            elif s[i] == '*':
                stars.append(i)
            else:
                if len(p) == 0 and len(stars) == 0:
                    return False
                if len(p) > 0:
                    n = p.pop()
                else:
                    n = stars.pop()
 
        while p and stars:
            if stars[-1] > p[-1]:
                stars.pop()
                p.pop()
            else:
                return False
        if len(p) > 0:
            return False
        return True
      