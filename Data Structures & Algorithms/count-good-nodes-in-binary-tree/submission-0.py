# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        
        def dfs(root):
            if root == None:
                return
            nonlocal ans
            ans += 1
            def worker(root, nodeSum):
                if root == None:
                    return
                if  root.val >= nodeSum:
                    nonlocal ans
                    ans += 1
                nodeSum = max(nodeSum,root.val)
                worker(root.left,nodeSum)
                worker(root.right, nodeSum)
            
            worker(root.left, root.val)
            worker(root.right, root.val)
        dfs(root)

        return ans
