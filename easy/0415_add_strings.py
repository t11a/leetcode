class Solution:
    def addStrings(self, num1, num2):
        return str(self._my_converter(num1) + self._my_converter(num2))

    def _my_converter(self, num):
        size = len(num)
        e = 0
        sum = 0

        for i in range(size):
            n = int(num[size-i-1])
            sum += n * 10 ** e
            e += 1

        return sum


print(Solution().addStrings('0', '0') == '0') # '0'
print(Solution().addStrings('1', '1') == '2') # '2'
print(Solution().addStrings('10', '25') == '35') # '35'