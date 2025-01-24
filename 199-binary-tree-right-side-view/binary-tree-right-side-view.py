# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        queue = deque()
        nextQueue = deque()
        queue.append(root)
        curr = []
        while queue:
            node = queue.popleft()
            curr.append(node.val)
            if node.left:
                nextQueue.append(node.left)
            if node.right:
                nextQueue.append(node.right)
            if len(queue) == 0:
                ans.append(curr[-1])
                curr = []
                queue = nextQueue
                nextQueue = deque()
        return ans