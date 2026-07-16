/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func goodNodes(root *TreeNode) int {
    var ans int = 0
    dfs(root,root.Val,&ans)
    return ans
}

func dfs(root *TreeNode, maxVal int, ans *int){
    if root == nil{
        return
    }

    if root.Val >= maxVal{
        *ans = *ans + 1
    }

    dfs(root.Right,max(root.Val,maxVal),ans)
    dfs(root.Left,max(root.Val,maxVal),ans)
    return
}
            

