# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.ans = None
        def dfs(node, p, q):
            if node == None:
                return
            if (node.val >= p.val and node.val <= q.val) or (node.val <= p.val and node.val >= q.val):
                self.ans = node
                return
            if (node.val >= p.val and node.val >= q.val):
                dfs(node.left,p,q)
            else:
                dfs(node.right,p,q)
        
        dfs(root,p,q)
        return self.ans