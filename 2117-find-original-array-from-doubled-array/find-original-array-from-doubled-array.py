class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        myMap = dict()
        result = []
        for n in changed:
            if n not in myMap:
                result.append(n)
                if 2*n not in myMap:
                    myMap[2*n] = 1
                else:
                    myMap[2*n] += 1
            else:
                myMap[n] -= 1
                if myMap[n] == 0:
                    del(myMap[n])
        if len(myMap) == 0:
            return result
        return [] 



        