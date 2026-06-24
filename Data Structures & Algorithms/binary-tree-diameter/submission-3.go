/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func diameterOfBinaryTree(root *TreeNode) int {
    ans := 0
    
    var dfs func(*TreeNode) int
    dfs = func(node *TreeNode) int {
        if node == nil {
            return 0
        }
        
        lSum := dfs(node.Left)
        rSum := dfs(node.Right)
        
        ans = max(ans, lSum+rSum)
        
        return max(lSum, rSum) + 1
    }
    
    dfs(root)
    return ans
}

