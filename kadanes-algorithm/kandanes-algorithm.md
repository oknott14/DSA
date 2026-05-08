## Kadane's Algorithm

---

### 1. Overview

Kadane's Algorithm solves the **Maximum Subarray Problem**: given an array of integers (which may include negatives), find the contiguous subarray that produces the largest sum.

It is remarkably elegant — a single linear scan through the array with O(n) time complexity and O(1) space. Before Kadane's, the brute-force approach checked every possible subarray, running in O(n²) or O(n³). Kadane's solved it optimally.

**Key facts:**
- Time complexity: **O(n)**
- Space complexity: **O(1)**
- Works on arrays with negative numbers, all-negatives, and mixed values
- Produces both the maximum sum AND the subarray indices (with slight modification)

---

### 2. How it Works

The core insight is a simple greedy decision made at every element: *is it better to extend the current subarray or start fresh from here?*

You maintain two variables as you scan left to right:

- `currentSum` — the best sum of a subarray ending at the current index
- `bestSum` — the best sum seen anywhere so far

At each index `i`:

```python
def kadane(arr):
    current_sum = arr[0]
    best_sum    = arr[0]
    best_start = best_end = cur_start = 0

    for i in range(1, len(arr)):
        # Start fresh, or extend?
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            cur_start   = i
        else:
            current_sum += arr[i]

        # Update global best
        if current_sum > best_sum:
            best_sum  = current_sum
            best_start = cur_start
            best_end   = i

    return best_sum, best_start, best_end
```

The decision `arr[i] > current_sum + arr[i]` simplifies to `current_sum < 0` — if the running sum has gone negative, any future element is better off starting a new subarray rather than dragging that dead weight along.

---

### 3. How to Identify the Pattern

Look for these signals in a problem statement:

- The phrase **"maximum/minimum subarray"** or **"largest/smallest sum of a contiguous subarray"**
- You're working with a **1D array** and need an optimal contiguous segment
- The array **contains negative numbers** (otherwise just sum everything)
- The problem asks about **subarrays**, not subsequences (contiguous matters)
- You need to optimize something **"over all possible windows"** without a fixed window size

A useful mental check: *"Can I make a greedy local decision at each element that leads to a globally optimal answer?"* If yes, Kadane's is likely involved.

---

### 4. Popular Sub-Patterns

**Maximum subarray (basic)** — the classic: return the largest contiguous sum. This is the canonical Kadane's problem.

**Minimum subarray** — flip the comparison operators. Track `currentMin` and `bestMin` instead. Equivalently, negate the array, run Kadane's, and negate the result.

**Maximum subarray with indices** — track `curStart`, `bestStart`, and `bestEnd` alongside the sums (as shown in the code above) to reconstruct which subarray produced the answer.

**Circular maximum subarray** — the subarray may wrap around the end of the array. The answer is either (a) the standard Kadane's result, or (b) `totalSum − minimumSubarraySum` (the complement trick). Take the max of both cases.

**Maximum product subarray** — instead of sums, maximize the product. Negative numbers flip signs, so you must track both the current maximum *and* current minimum at each step (a negative minimum × a negative number = a new maximum).

**2D maximum subarray** — extend to a matrix. Fix the left and right column boundaries, collapse each row into a 1D prefix sum, then run Kadane's on that 1D array. Runs in O(n²·m).

---

### 5. Practice Questions

Work through these roughly in order of difficulty:

1. **Maximum Subarray** (LeetCode 53) — the canonical problem. Start here.
2. **Maximum Sum Circular Subarray** (LeetCode 918) — apply the complement trick.
3. **Maximum Product Subarray** (LeetCode 152) — track both max and min.
4. **Minimum Subarray Sum** — flip the comparisons; good for solidifying the pattern.
5. **Subarray Sum Equals K** (LeetCode 560) — not Kadane's directly, but a natural next step using prefix sums.
6. **Maximum Sum of Two Non-Overlapping Subarrays** (LeetCode 1031) — run Kadane's from left and right, combine.
7. **Maximum Absolute Sum of Any Subarray** (LeetCode 1749) — find both max and min subarrays, take the larger absolute value.
8. **Maximum Sum Rectangle in a 2D Matrix** — implement the full 2D extension.

Use the interactive widget above to step through your own examples — try an all-negative array, or one that resets multiple times, to build intuition for when and why the algorithm starts fresh.