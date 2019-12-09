class Solution:
    def romanToInt(self, s: str):
        romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        prev_val = 0
        ans = 0

        for i in range(len(s)-1, -1, -1):
            int_val = romans[s[i]]
            if int_val < prev_val:
                ans -= int_val
            else:
                ans += int_val
            print("{},{},{}".format(prev_val, int_val, ans))
            prev_val = int_val

        return ans

print(Solution().romanToInt('III') == 3)
print(Solution().romanToInt('IV') == 4)
print(Solution().romanToInt('IX') == 9)
print(Solution().romanToInt('XI') == 11)
print(Solution().romanToInt('LVIII') == 58)
print(Solution().romanToInt('MCMXCIV') == 1994)