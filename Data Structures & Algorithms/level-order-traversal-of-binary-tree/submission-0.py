# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()


        q.append(root)
        ot = []
        while len(q) > 0:
            qlen = len(q)
            res= []
            for i in range(qlen):
                head = q.popleft()
                if head:
                    res.append(head.val)
                    q.append(head.left)
                    q.append(head.right)
            if res:
                ot.append(res)
            # print(re/s)
        return ot