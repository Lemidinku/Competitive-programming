# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def validate(node):
            if not node:
                return True, -inf, inf

            ans = True

            left_valid, left_max, left_min = validate(node.left)
            right_valid, right_max, right_min = validate(node.right)

            ans &= left_max < node.val < right_min
            ans &= left_valid & right_valid
            maxx = max(left_max, node.val, right_max)
            minn = min(left_min, node.val, right_min)

            return ans, maxx, minn

        valid, _, _ = validate(root)

        return valid
