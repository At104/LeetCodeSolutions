class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        bottle = numBottles
        while numBottles > 0:
            empty = empty + numBottles
            numBottles = empty//numExchange
            empty = empty%numExchange
            bottle += numBottles
        return bottle
    
c = Solution()
print(c.numWaterBottles(15,4))