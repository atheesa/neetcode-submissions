/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


type Queue struct {
    list []*TreeNode
}
   func (q *Queue) popleft() *TreeNode {
       if len(q.list) == 0 {
           return nil
       }
       first := q.list[0]
       q.list = q.list[1:]
       return first
   }
func (q *Queue) append(node *TreeNode) {
    q.list = append(q.list,node)
}
func (q *Queue) peekleft() *TreeNode{
    return q.list[0] 
}

func (q *Queue) peekright() *TreeNode{
    if len(q.list) == 0 {
        return nil
    }
    return q.list[len(q.list)-1]
}

func rightSideView(root *TreeNode) []int {
    if root == nil{
        return []int{}
    }
    var ans []int = []int{}
    var q *Queue = &Queue{}
    q.append(root)

    for len(q.list) >0 {
        qLen := len(q.list)
        ans = append(ans,q.peekright().Val)
        for i := 0; i < qLen; i++ {
           node := q.popleft()
           if node.Left != nil {
            q.append(node.Left)
           }
           if node.Right != nil {
            q.append(node.Right)
           } 
        }
    }

    return ans    


}
