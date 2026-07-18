class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        median = len(palindrome) // 2
        for i in range(len(palindrome)):
            if i == median:
                palindrome[len(palindrome)-1] = 'b'
                break

            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                break
            else:
                continue
        return "".join(palindrome)
            
                

