from typing import List


class Solution:
    def buildAdjList(self, numCourses: int, prerequisites: List[List[int]]):
        adj = [[] for i in range(numCourses)]

        for [course, pre_req] in prerequisites:
            adj[pre_req].append(course)

        return adj

    def khan(self, numCourses: int, inDegrees: List[int], adj: List[List[int]]) -> bool:
        queue = []

        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            curr = queue.pop(0)
            count += 1

            for next in adj[curr]:
                inDegrees[next] -= 1

                if inDegrees[next] == 0:
                    queue.append(next)

        return count == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = self.buildAdjList(numCourses, prerequisites)
        inDegrees = [0] * numCourses

        for v1, v2 in prerequisites:
            inDegrees[v1] += 1

        return self.khan(numCourses, inDegrees, adj)


soln = Solution()


def test_case_1():
    numCourses = 2
    prerequisites = [[1, 0]]
    assert soln.canFinish(numCourses, prerequisites)


def test_case_2():
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    assert not soln.canFinish(numCourses, prerequisites)


def test_no_prerequisites():
    numCourses = 10
    prerequisites = []
    assert soln.canFinish(numCourses, prerequisites)


def test_long_prerequisite_chain():
    numCourses = 8
    prerequisites = [[0, 1], [1, 4], [4, 3], [3, 5], [5, 6], [6, 2], [2, 7]]
    assert soln.canFinish(numCourses, prerequisites)


def test_long_loop_prerequisite_chain():
    numCourses = 8
    prerequisites = [[0, 1], [1, 4], [4, 3], [3, 5], [5, 6], [6, 2], [2, 7], [7, 1]]
    assert not soln.canFinish(numCourses, prerequisites)
