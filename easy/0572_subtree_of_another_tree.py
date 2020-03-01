# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self._isMatch(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def _isMatch(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        else:
            return self._isMatch(s.left, t.left) and self._isMatch(s.right, t.right)

s = TreeNode(1)
t = TreeNode(1)
print( Solution().isSubtree(s, t) )
