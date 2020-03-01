class Solution:

    def _make_hist(self, s: str):
        hist = {}
        for i in range(0, len(s)):
            key = s[i]
            if hist.get(key):
                hist[key] += 1
            else:
                hist[key] = 1
        return hist

    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        hist_s = self._make_hist(s)
        hist_t = self._make_hist(t)

        for k in hist_s:
            if hist_t.get(k):
                if hist_t.get(k) != hist_s.get(k):
                    return False
            else:
                return False

        return True

print(Solution().isAnagram('anagram', 'nagaram')) # true
print(Solution().isAnagram('rat', 'cat')) # false
print(Solution().isAnagram('rat', 'ca')) # false
