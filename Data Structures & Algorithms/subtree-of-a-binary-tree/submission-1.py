# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.ans = False 

        def dfs(root1):
            if root1 == None:
                return
            t = self.isSameSubTree(root1,subRoot)
            if t == True:
                self.ans = True
            dfs(root1.left)
            dfs(root1.right)
            return
        dfs(root)
        return self.ans
            



    def isSameSubTree(self,root1, root2):
        if root1 == None and root2 == None:
            return True
        
        if (root1 == None or root2 == None) or (root1.val != root2.val):
            return False

        return self.isSameSubTree(root1.left,root2.left) and self.isSameSubTree(root1.right,root2.right)


                

