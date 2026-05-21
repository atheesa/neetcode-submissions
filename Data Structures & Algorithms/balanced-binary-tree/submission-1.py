# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.isBalancedBool = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.isBalancedBool

    def dfs(self,root) -> int:
        if root == None:
            return 0
        l1 = self.dfs(root.left)
        r1 = self.dfs(root.right)
        if abs(r1 - l1) > 1:
            self.isBalancedBool = False
        return max(l1,r1) + 1

