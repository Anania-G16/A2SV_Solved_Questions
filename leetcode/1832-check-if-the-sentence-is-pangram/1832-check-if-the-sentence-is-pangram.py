class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        mySet = set()
        for ch in sentence:
            if ch not in mySet:
                mySet.add(ch)
        return True if len(mySet) == 26 else False