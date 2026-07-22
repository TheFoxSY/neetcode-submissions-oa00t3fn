class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        res = []
        finished = 0

        for cour, pre in prerequisites:
            indegree[cour] += 1
            course[pre].append(cour)
        
        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            cur_course = q.popleft()
            res.append(cur_course)
            finished += 1
            for courses in course[cur_course]:
                indegree[courses] -= 1
                if indegree[courses] == 0:
                    q.append(courses)
        
        if finished != numCourses:
            return []
        return res
            

