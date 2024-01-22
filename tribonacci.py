class Solution:
    store = {}
    def tribonacci(self, n: int) -> int:
        if n in self.store:
            return self.store[n]
        if n == 0:
            result = 0
        elif n==1 or n==2:
            result = 1
        else:
            result = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            self.store[n] = result
        return result

c = Solution()
print(c.tribonacci(100))