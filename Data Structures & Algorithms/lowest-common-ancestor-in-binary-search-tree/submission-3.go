/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func lowestCommonAncestor(root *TreeNode, p *TreeNode, q *TreeNode) *TreeNode {

    return dfs(root,p,q)

}

func dfs(root *TreeNode, p *TreeNode, q *TreeNode) *TreeNode{
    if root == nil{
        return nil

    }
    if (root.Val >= p.Val && root.Val <= q.Val) || (root.Val <= p.Val && root.Val >= q.Val) {
        return root
    }
    if (root.Val >= p.Val && root.Val >= q.Val){
        return dfs(root.Left,p,q)
    } else {
        return dfs(root.Right,p,q)
    }
    return nil
}