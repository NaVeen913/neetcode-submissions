# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        res = 0
        def depth(root):
            if not root:
                return 0

            left = depth(root.left)
            right = depth(root.right)

            #do something for diameter
            nonlocal res
            res = max(res, left + right)
            return  1 + max(left, right)
        depth(root)
        return res

        # dia = self.depth(root?)
        # return max((1 + self.diameterOfBinaryTree(root.left)), 1 + self.diameterOfBinaryTree(root.right))