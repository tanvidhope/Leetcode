class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        outdegree = [0]*numCourses
        coursesTaken = 0
        for prereq in prerequisites:
            graph[prereq[0]].add(prereq[1])
            outdegree[prereq[0]]+=1
        queue = deque()
        for i in range(numCourses):
            if outdegree[i] == 0:
                queue.append(i)
                coursesTaken+=1
        while queue:
            c = queue.popleft()
            for course in graph:
                if c in graph[course]:
                    outdegree[course]-=1
                    if outdegree[course] == 0:
                        queue.append(course)
                        coursesTaken+=1
        return coursesTaken == numCourses
        