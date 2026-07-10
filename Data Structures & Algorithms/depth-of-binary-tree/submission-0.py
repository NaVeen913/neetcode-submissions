# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if not root:
            return 0

        q.append(root)
        maxDepth = 0
        while q:
            lenq = len(q)
            for _ in range(lenq):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            maxDepth += 1
        return maxDepth
