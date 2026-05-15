# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if self.isSubTreeHelper(root,subRoot):
            return True
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)
        
        return left or right


    def isSubTreeHelper(self,r1,r2):
        if r1 == None and r2 == None:
            return True
        if r1 == None or r2 == None:
            return False
        if r1.val != r2.val:
            return False
        left = self.isSubTreeHelper(r1.left,r2.left)
        right = self.isSubTreeHelper(r1.right,r2.right)

        return left and right
