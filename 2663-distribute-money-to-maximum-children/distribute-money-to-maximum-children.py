class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1
        temp = money
        x = money // 7
        rem = temp % 7
        if money > children * 7:
            return children-1
        if x == children - 1 and rem == 3:
            return x-1
        return x
        

    
       