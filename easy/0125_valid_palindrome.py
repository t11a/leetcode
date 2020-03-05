import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove chars excpet alphanumeric chars and lower the cases
        s = re.sub('[^0-9a-zA-Z]', "", s).lower()

        size = len(s)
        for i in range(0, int(size/2)):
            if s[i] == s[size-1-i]:
                pass
            else:
                return False

        return True

# Input: "A man, a plan, a canal: Panama"
# Output: true
print(Solution().isPalindrome("A man, a plan, a canal: Panama")) # True

# Input: "race a car"
# Output: false
print(Solution().isPalindrome("race a car")) # False