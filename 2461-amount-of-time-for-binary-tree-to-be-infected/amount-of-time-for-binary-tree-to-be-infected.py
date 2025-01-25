# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        #bfs
        adjList = defaultdict(set)
        self.createGraph(adjList, root, 0)
        queue = deque()
        queue.append(start)
        visited = set()
        time = 0
        visited.add(start)
        while(len(queue)>0):
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                for neighbour in adjList[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            time+=1
        return time-1

    def createGraph(self, adjList, root, parent):
        if (root==None):return
        if root.val not in adjList:
            adjList[root.val] = set()
        if parent != 0:
            adjList[root.val].add(parent)
        if root.left != None:
            adjList[root.val].add(root.left.val)
        if root.right != None:
            adjList[root.val].add(root.right.val)
        self.createGraph(adjList, root.left, root.val)
        self.createGraph(adjList, root.right, root.val)