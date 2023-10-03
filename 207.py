from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {course: [] for course in range(numCourses)}

        for course1, course2 in prerequisites:
            prereqMap[course1].append(course2)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prereqMap[course] == []:
                return True

            visited.add(course)

            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            prereqMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
