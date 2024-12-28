# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            # replace with right child ka leftmost node
            if not root.right:
                return root.left
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val, temp.val= temp.val, root.val
            root.right = self.deleteNode(root.right, key)
        elif root.val<key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left= self.deleteNode(root.left, key)
        return root