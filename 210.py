from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencyMap = {course: [] for course in range(numCourses)}

        for course, depCourse in prerequisites:
            dependencyMap[course].append(depCourse)

        result, resultSet = [], set()
        visited = set()

        # Find possible path
        def dfs(course: int) -> bool:
            if course in visited:
                return False
            if course in resultSet:
                return True

            visited.add(course)

            for dep in dependencyMap[course]:
                if not dfs(dep):
                    return False

            visited.remove(course)

            result.append(course)
            resultSet.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result
