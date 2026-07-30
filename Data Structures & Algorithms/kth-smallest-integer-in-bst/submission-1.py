# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 1
        self.ans = None

        def dfs(node,k):
            if node == None:
                return

            dfs(node.left,k)

            if self.count == k:
                self.ans = node.val
                self.count += 1
                return

            self.count += 1

            dfs(node.right,k)

            return
        dfs(root,k)
        return self.ans