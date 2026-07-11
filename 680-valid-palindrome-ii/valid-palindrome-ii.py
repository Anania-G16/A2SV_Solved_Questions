class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        canDelete = True

        def isPalindrome(left, right):
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if isPalindrome(left + 1, right):
                    return True
                elif isPalindrome(left, right - 1):
                    return True
                else:
                    return False
        return True
