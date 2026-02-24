class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        myDict = dict()
        mySet = set()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if  pattern[i] not in myDict:
                if words[i] in mySet:
                    return False
                myDict[pattern[i]] = words[i]
                mySet.add(words[i])
            else:
                if myDict[pattern[i]] != words[i]:
                    return False
        return True