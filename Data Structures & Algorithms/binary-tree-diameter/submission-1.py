# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):  
            if root == None:
                return 0
            lSum = dfs(root.left)
            rSum = dfs(root.right)
            self.ans = max(lSum + rSum, self.ans) 
            return max(lSum, rSum) + 1

        dfs(root)
        return self.ans

        