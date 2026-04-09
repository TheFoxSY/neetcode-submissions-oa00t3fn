class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {course: [] for course in range(numCourses)}
        for a, b in prerequisites:
            prevMap[a].append(b)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False 
            if prevMap[course] == []:
                return True
            
            visited.add(course)
            for pre in prevMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            prevMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

        

        


        