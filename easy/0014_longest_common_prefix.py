class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        min_len = float('inf')
        shortest = ""
        for i, word in enumerate(strs):
            if len(word) < min_len:
                min_len = len(word)
                shortest = word

        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

print(Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl")
print(Solution().longestCommonPrefix(["dog","racecar","car"]) == "")