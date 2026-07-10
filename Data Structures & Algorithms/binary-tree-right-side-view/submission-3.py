# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque()
        # if root:
        q.append(root)

        while q:
            rightside = None #why this ?
            qlen = len(q)
            print(qlen)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightside = node ## since it is in the loop will get overridden by the last element
                    # res.append(node.val)
                    q.append(node.left)  
                    q.append(node.right)  
            if rightside:
                res.append(rightside.val)
        return res
        