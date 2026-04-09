class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path , visited = set(), set()
        prevMap = {courses : [] for courses in range(numCourses)}
        res = []
        for course,pre in prerequisites:
            prevMap[course].append(pre) 

        def dfs(course):
            if course in visited:
                return True
            if course in path:
                return False
            
            path.add(course)
            for pre in prevMap[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            visited.add(course)
            res.append(course)
            return True 
        
        for c in range(numCourses):
            if not dfs(c):
                return []  
        return res
        