# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        q = deque([root])
        visited = set()
        
        while q:
            local = []
            for _ in range(len(q)):
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                local.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(local)
        return res