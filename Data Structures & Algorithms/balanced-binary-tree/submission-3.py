# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        val, ans = self.dfs(root)
        return ans
    def dfs(self, n):
        if n == None:
            return 0, True
        left_value, left_signal = self.dfs(n.left)
        right_value, right_signal = self.dfs(n.right)
        if (abs(left_value - right_value) > 1):
            return -1, False
        else:
            return max(left_value,right_value) + 1 , (left_signal and right_signal and True)
        # left value
        # right value
        # is abs(left - right) > 0:
        #    return False
        # else:
        #   return True
