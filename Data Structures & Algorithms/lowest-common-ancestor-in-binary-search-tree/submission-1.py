# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root, p, q):
            if root == None:
                return
            elif root.val > p.val and root.val > q.val:
                return dfs(root.left,p,q)
            elif root.val < p.val and root.val < q.val:
                return dfs(root.right, p, q)
            return root
        
        ans = dfs(root,p,q)
        return ans