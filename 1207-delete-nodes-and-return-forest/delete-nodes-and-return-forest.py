# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDelete = set(to_delete)
        forest = []
        root = self.process(root, toDelete, forest)
        if root:
            forest.append(root)
        return forest
    
    def process(self, node, toDelete, forest):
        if not node:
            return None
        node.left = self.process(node.left, toDelete, forest)
        node.right = self.process(node.right, toDelete, forest)
        if node.val in toDelete:
            if node.left:
                forest.append(node.left)
            if node.right:
                forest.append(node.right)
            return None
        return node