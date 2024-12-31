# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # you need 3 things - 
        # the height of subtree rooted at each node
        # the level of each node
        # and the top2 heights at each level
        # for every query, you can then look at the top 2 heights in the level
        subtreeHeights = defaultdict(int)
        nodeLevels = defaultdict(int)

        levelHeights = defaultdict(list)

        def dfs(node, level):
            if not node:
                return 0
            nodeLevels[node.val] = level
            leftHeight = dfs(node.left, level+1)
            rightHeight = dfs(node.right, level+1)
            currHeight = 1+max(leftHeight, rightHeight)
            subtreeHeights[node.val] = currHeight
            if not levelHeights[level]:
                levelHeights[level] = [0,0]
            if currHeight > levelHeights[level][0]:
                levelHeights[level][1] = levelHeights[level][0]
                levelHeights[level][0] = currHeight
            elif currHeight > levelHeights[level][1]:
                levelHeights[level][1] = currHeight
            return currHeight
        
        dfs(root, 0)
        return [nodeLevels[q] + (levelHeights[nodeLevels[q]][1] if subtreeHeights[q] == levelHeights[nodeLevels[q]][0] else levelHeights[nodeLevels[q]][0])-1
        for q in queries]