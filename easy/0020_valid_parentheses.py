class Solution:
    def isValid(self, s):
        stack = []

        mappings = {')' : '(', ']' : '[', '}' : '{'}

        for ch in s:
            if ch in mappings:
                if not stack:
                    return False

                top_elm = stack.pop()
                
                if top_elm != mappings[ch]:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0

print(Solution().isValid('()'))
print(Solution().isValid('()[]{}'))
print(Solution().isValid('([)]'))
print(Solution().isValid('{[]}'))