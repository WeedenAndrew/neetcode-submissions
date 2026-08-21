# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return [None]

        left = self.traversal(root.left)
        right = self.traversal(root.right)
        return [root.val] + left + right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traversal(p) == self.traversal(q) 