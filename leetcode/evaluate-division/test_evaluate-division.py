from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        nodes = defaultdict(dict)
        results = []
        
        for idx in range(len(equations)):
            a, b = equations[idx]
            ans = values[idx]

            nodes[a][b] = ans
            if ans != 0:
                nodes[b][a] = 1 / ans

        def dfs(curr: str, end: str, val: float) -> bool:
            if curr not in nodes or curr in visited:
                return False
            elif curr == end:
                results.append(val)
                return True

            visited.add(curr)
            for nxt, cost in nodes[curr].items():
                if dfs(nxt, end, val * cost):
                    return True

            return False

        visited = set()
        for curr, end in queries:
            if not dfs(curr, end, 1):
                results.append(-1.0)
            visited.clear()
        return results


soln = Solution()


def test_case_1():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    assert soln.calcEquation(equations, values, queries) == [
        6.00000,
        0.50000,
        -1.00000,
        1.00000,
        -1.00000,
    ]


def test_case_2():
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    assert soln.calcEquation(equations, values, queries) == [
        3.75000,
        0.40000,
        5.00000,
        0.20000,
    ]


def test_case_3():
    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    assert soln.calcEquation(equations, values, queries) == [
        0.50000,
        2.00000,
        -1.00000,
        -1.00000,
    ]

def test_long_resolution():
    equations =[
        ['a','b'],
        ['b','c'],
        ['c','d'],
        ['d','e'],
        ['e','f']
    ]
    values = [2., 2., 2., 3., 4.]
    queries = [['a','f']]
    assert soln.calcEquation(equations, values, queries) == [96.]