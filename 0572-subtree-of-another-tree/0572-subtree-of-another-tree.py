# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isIdentical(node, target):
            if not (node or target): return True
            if not(node and target): return False
            return node.val == target.val and isIdentical(node.left, target.left) and isIdentical(node.right, target.right)

        def check(node, target):
            if not node: return False
            
            return  isIdentical(node, target) | check(node.left, target) | check(node.right, target)

        return check(root, subRoot)