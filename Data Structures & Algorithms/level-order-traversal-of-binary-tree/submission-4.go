/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Queue struct {
    items [] *TreeNode
}

func (q *Queue) enqueue(node *TreeNode) {
    q.items = append(q.items,node)
}

func (q *Queue) deque() *TreeNode {
    first := q.items[0]
    q.items = q.items[1:]
    return first

}


func levelOrder(root *TreeNode) [][]int {
    if root == nil  {
        return [][]int{}
    }
    ans := [][]int{}


    queue := &Queue{}
    queue.enqueue(root)
    curr := 0

    for len(queue.items) > 0 {
        qLen := len(queue.items)
        ans = append(ans,[]int{})
        for i := 0; i < qLen; i++{
            node := queue.deque()
            ans[curr] = append(ans[curr],node.Val)
            if node.Left != nil{
                queue.enqueue(node.Left)
            }
            if node.Right != nil {
                queue.enqueue(node.Right)
            }
        }
        curr = curr + 1

    }

    return ans
}
