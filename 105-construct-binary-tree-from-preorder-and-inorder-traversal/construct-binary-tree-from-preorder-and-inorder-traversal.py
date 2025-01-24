# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def arrayToTree(left, right):
            nonlocal preorderIndex
            if left > right :
                return None
            
            rootVal = preorder[preorderIndex]
            root = TreeNode(rootVal)
            preorderIndex+=1
            root.left = arrayToTree(left, inorderIndexMap[rootVal]-1)
            root.right = arrayToTree(inorderIndexMap[rootVal]+1, right)
            return root

        preorderIndex = 0
        inorderIndexMap = {}
        for i, val in enumerate(inorder):
            inorderIndexMap[val] = i
        return arrayToTree(0, len(preorder)-1)
