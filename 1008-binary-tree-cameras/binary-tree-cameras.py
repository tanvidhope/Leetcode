# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 3 things, 0 = covered, 1 = camera, 2 = needsCover
        self.numCameras = 0
        return self.numCameras+1 if self.cover(root) == 2 else self.numCameras

    def cover(self, root):
        if root == None:
            return 0
        left = self.cover(root.left)
        right = self.cover(root.right)
        if left == 2 or right == 2:
            self.numCameras+=1
            return 1
        if left == 1 or right == 1:
            return 0
        return 2