class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        myMap = dict()
        count = 0
        for n in answers:
            if n not in myMap:
                myMap[n] = 1
                count += n+1
                if myMap[n] == n+1:
                    del(myMap[n])
            else:
                myMap[n] += 1
                if myMap[n] == n+1:
                    del(myMap[n])
        return count



        