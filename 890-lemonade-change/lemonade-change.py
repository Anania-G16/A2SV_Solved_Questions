class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        running_sum = 0
        fiveCount = 0
        tenCount = 0
        for n in bills:
            if n == 20:
                if running_sum < n-5:
                    return False
                if tenCount == 0:
                    if fiveCount < 3:
                        return False
                    else:
                        fiveCount -= 3
                else:
                    if fiveCount == 0:
                        return False
                    else:
                        tenCount -= 1
                        fiveCount -= 1
            elif n == 10:
                if running_sum < n-5:
                    return False
                if fiveCount == 0:
                    return False
                else:
                    fiveCount -= 1
                    tenCount += 1
            else:
                fiveCount += 1
            running_sum += n
        return True    
        
        
        





        