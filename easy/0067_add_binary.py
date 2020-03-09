class Solution:
    def addBinary(self, a, b):
        max_size = max(len(a), len(b))

        a = a.zfill(max_size)
        b = b.zfill(max_size)

        carry = 0
        ans = ""

        for i in range(max_size-1, -1, -1):
            if a[i] == "1":
                carry += 1 
            if b[i] == "1":
                carry += 1

            # set ans
            # carry : 0, 1, 2
            # 0, 2 -> 0
            # 1 -> 1
            if carry % 2 == 0:
                ans = "0" + ans
            else:
                ans = "1" + ans

            # update carry
            # 0, 1 -> 0
            # 2 -> 1
            carry = int(carry/2)

        # if carry == 1, then add '1' as prefix
        if carry == 1:
            ans = "1" + ans

        print(ans)
        return ans

print(Solution().addBinary("11", "1") == "100")
print(Solution().addBinary("1010", "1011") == "10101")