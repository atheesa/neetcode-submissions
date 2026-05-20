# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def dfs(root) -> int:
            if root == None:
                return 0
            l1 = dfs(root.left)
            r2 = dfs(root.right)
            self.ans = max(self.ans,l1 + r2)

            return max(l1,r2) + 1
        dfs(root)
        return self.ans
