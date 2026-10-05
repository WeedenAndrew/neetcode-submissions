# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        if root:
            l.extend(self.postorderTraversal(root.left))
            l.extend(self.postorderTraversal(root.right))
            l.append(root.val)
        return l