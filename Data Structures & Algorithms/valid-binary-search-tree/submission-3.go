/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValidBST(root *TreeNode) bool {
    res := []int{}
    return dfs(root,&res)
}

func dfs(root *TreeNode, res *[]int) bool {
    if root == nil{
        return true
    }

    lfs := dfs(root.Left,res)
    if len(*res) > 0 && (*res)[len(*res)-1] >= root.Val{
        return false
    }
    *res = append(*res,root.Val)
    rfs := dfs(root.Right,res)
    return lfs && rfs
}
