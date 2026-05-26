# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        depthNode = []
        ans = []

        while(q):
            qLen = len(q)
            temp = []
            for n in range(qLen): 
                node = q.popleft()
                if node:
                    temp.append(node)
                    q.append(node.left)
                    q.append(node.right)
            if temp:
                ans.append(temp.pop().val)
                depthNode.append(temp)
        return ans
            
        