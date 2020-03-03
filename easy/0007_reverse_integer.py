class Solution:
    def reverse(self, x):
        ans = 0
        x_s = str(x)
        if x_s[0] == '-':
            ans = -(int(x_s[1:][::-1]))
        else:
            ans = int(x_s[::-1])

        if ans > 2**31 -1 or ans < -2**31:
            return 0
        
        return ans

print(Solution().reverse(123)) # 321
print(Solution().reverse(-123)) # -321
print(Solution().reverse(120)) # 21