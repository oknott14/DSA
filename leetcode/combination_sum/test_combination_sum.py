from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(remainder: int, curr: List[int], c_idx: int):
            if 0 == remainder:
                ans.append(curr.copy())
                return
            for idx in range(c_idx, len(candidates)):
                if remainder < candidates[idx]:
                    continue

                curr.append(candidates[idx])
                backtrack(remainder - candidates[idx], curr, idx)
                curr.pop(-1)

        backtrack(target, [], 0)
        return ans


soln = Solution()


def test_case_1():
    # 7 G
    # 6 => 2 X
    # 3 => 3 => 2 X
    # 3 => 2 => 2 G
    # 2 => 2 => 2 => 2 X
    candidates = [2, 3, 6, 7]
    target = 7
    output = [[2, 2, 3], [7]]

    assert soln.combinationSum(candidates, target) == output


def test_case_2():
    candidates = [2, 3, 5]
    target = 8
    output = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    assert soln.combinationSum(candidates, target) == output
