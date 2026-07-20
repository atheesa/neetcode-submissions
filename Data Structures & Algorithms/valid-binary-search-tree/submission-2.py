# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.res = []

        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            if self.res and self.res[-1] >= node.val:
                self.ans = False
            self.res.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        return self.ans