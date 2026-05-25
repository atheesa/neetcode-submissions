# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque([root])
        ans = []

        while q:
            temp = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node == None:
                    break
                temp.append(node.val)
                leftNode = node.left
                rightNode = node.right
                if leftNode:
                    q.append(leftNode)
                if rightNode:
                    q.append(node.right)
            if temp:
                ans.append(temp[::])
        return ans