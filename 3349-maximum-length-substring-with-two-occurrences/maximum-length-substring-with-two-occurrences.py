class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        myMap = defaultdict(int)
        lastOccurence = defaultdict(int)
        count = 0
        left = 0
        right = 0
        while right < len(s):
            if myMap[s[right]] < 2:
                myMap[s[right]] += 1
                lastOccurence[s[right]] = right
                right += 1
            else:
                count = max(count, right - left)
                while left < right:
                    myMap[s[left]] -= 1
                    if s[left] == s[right]:
                        left += 1
                        break
                    left += 1
        
        count = max(count, right - left)
        return count
        
            