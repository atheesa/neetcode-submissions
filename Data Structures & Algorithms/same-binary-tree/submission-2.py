# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)

    def dfs(self,root1, root2) -> bool:
        if root1 == None and root2 == None:
            return True
        elif (root1 == None or root2 == None):
            return False
        elif (root1.val != root2.val):
            return False
        return self.dfs(root1.left, root2.left) and self.dfs(root1.right, root2.right)  