class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaterIndex = 0
        radius = 0
        heaters.sort()
        houses.sort()
        for house in houses:
            
            while heaterIndex < len(heaters)-1 and abs(house - heaters[heaterIndex]) >= abs(house - heaters[heaterIndex+1]):
                heaterIndex += 1
                    
            firsthrad = abs(heaters[heaterIndex]-house)

            if heaterIndex == len(heaters)-1:
                secondhrad = float('inf')
            else:
                secondhrad = abs(heaters[heaterIndex+1]-house)
                
            radius = max(radius, min(firsthrad, secondhrad))

        return radius