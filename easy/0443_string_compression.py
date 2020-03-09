class Solution:
    def compress(self, chars):
        walker, runner = 0, 0
        while runner < len(chars):
            chars[walker] = chars[runner]
            count = 1

            while runner+1 < len(chars) and chars[runner] == chars[runner+1]:
                runner += 1
                count += 1

            if count > 1:
                for c in str(count):
                    chars[walker+1] = c
                    walker += 1

            print("{} {} {}".format(walker, runner, chars))
            walker += 1
            runner += 1
        
        return walker


print(Solution().compress(["a","a","b","b","c","c","c"]) == 6)
print(Solution().compress(["a"]) == 1)
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4)
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","c"]) == 5)
