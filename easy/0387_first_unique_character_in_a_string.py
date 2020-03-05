class Solution:
    def firstUniqChar(self, s: str) -> int:
        word = {}
        for ch in s:
            word[ch] = word.get(ch, 0) + 1

        ans = 0
        for ch in s:
            if word[ch] == 1:
                break
            ans += 1

        if ans == len(s):
            ans = -1

        return ans

print(Solution().firstUniqChar("leetcode")) # 0
print(Solution().firstUniqChar("loveleetcode")) # 2
print(Solution().firstUniqChar("abcdefabcdef")) # -1
