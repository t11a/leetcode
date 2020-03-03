class Solution:
    def addDigits(self, num: int) -> int:
        n = num
        while n >= 10:
            summ = 0
            while n > 0:
                summ += n % 10
                n = int(n / 10)
            n = summ

        return n

print(Solution().addDigits(38)) # 3 + 8 = 11, 1 + 1 = 2, ans = 2