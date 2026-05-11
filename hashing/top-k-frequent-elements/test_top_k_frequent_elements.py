import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        results = []
        
        for key, count in counts.items():
            
            results.append((count, key))
            heapq.heapify(results)

            if len(results) > k:
                heapq.heappop(results)

        return [r[1] for r in results]
    

soln = Solution()

def test_case_1():
    
    assert soln.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [2, 1]

def test_single_elt():
    assert soln.topKFrequent([1], 10) == [1]

def test_case_3():
    assert soln.topKFrequent([1,2,1,2,1,2,3,1,3,2], k = 2) == [1,2]