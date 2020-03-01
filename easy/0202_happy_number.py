class Solution:
    def isHappy(self, n: int) -> bool:
        h = {}

        current = n

        while current != 1:
            current = self._digit_square(current)
            if current in h.keys():
                # loop is detected.
                return False
            else:
                h[current] = 0

        return True

    def _digit_square(self, n):
        s = str(n)
        size = len(s)

        sum = 0
        for i in range(0, size):
            d = int(s[i])
            sum += d*d
            
        return sum

print(Solution().isHappy(19)) # True