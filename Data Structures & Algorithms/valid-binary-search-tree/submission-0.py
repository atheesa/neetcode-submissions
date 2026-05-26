# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = True
        sortedBST = []
        def dfs(root):
            if (root == None):
                return
            dfs(root.left)
            sortedBST.append(root.val)
            dfs(root.right)
        dfs(root)
        if len(sortedBST) == 1:
            return True
        return all(sortedBST[i + 1] > sortedBST[i] for i in range(len(sortedBST)-1))
