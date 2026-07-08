class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = (len(s)+1) * [0]
        prefix = diff.copy()
        s_list = list(s)
        for shift in shifts:
            if shift[2] == 1:
                diff[shift[0]] += 1
                diff[shift[1] + 1] +=  -1
                
            else:
                diff[shift[0]] += -1
                diff[shift[1] + 1] += 1

        running_sum = 0
        for i in range(len(s)):
            running_sum += diff[i]
            prefix[i] = running_sum
        
        for i in range(len(s)):
            s_list[i] = chr((ord(s[i]) - ord('a') + prefix[i]) % 26 + ord('a'))        
        s = "".join(s_list)
        return s

