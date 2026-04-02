# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if curr == None:
                return 0

            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)
            self.res = max(self.res, leftMax + rightMax)
            return max(leftMax, rightMax) + 1 
        dfs(root)
        return self.res
        