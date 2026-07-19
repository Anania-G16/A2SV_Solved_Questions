class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        sumArray = []
        aliceTurn = True
        result = 0
        for i in range(len(aliceValues)):
            sumArray.append(aliceValues[i] + bobValues[i])
        sumArray = list(enumerate(sumArray))
        sumArray.sort(key = lambda x: x[1], reverse = True)
        for index, item in sumArray:
            if aliceTurn:
                result += aliceValues[index]
            else:
                result -= bobValues[index]
            aliceTurn = not aliceTurn
            
        if result > 0:
            return 1
        elif result < 0:
            return -1
        else:
            return 0
        return 100