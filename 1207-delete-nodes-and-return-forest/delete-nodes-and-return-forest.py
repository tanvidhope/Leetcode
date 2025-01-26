# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        toDelete = set(to_delete)
        root = self.dfs(root, toDelete)
        if root:
            self.ans.append(root)
        return self.ans
    
    def dfs(self, root, toDelete):
        if not root:
            return
        root.left = self.dfs(root.left, toDelete)
        root.right = self.dfs(root.right, toDelete)
        if root.val in toDelete:
            if root.left:
                self.ans.append(root.left)
            if root.right:
                self.ans.append(root.right)
            return None
        return root