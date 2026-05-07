# Prefix Sum

## 1. Overview

The **Prefix Sum** pattern (also called _Cumulative Sum_) is a preprocessing technique that transforms an array into a new array where each element stores the sum of all previous elements up to that index. This allows **range sum queries** to be answered in **O(1)** time after an **O(n)** preprocessing step — instead of recomputing sums from scratch each time.

| Operation       | Brute Force | Prefix Sum |
| --------------- | ----------- | ---------- |
| Preprocessing   | O(1)        | O(n)       |
| Range Sum Query | O(n)        | O(1)       |
| Space           | O(1)        | O(n)       |

It is one of the most powerful and underrated patterns — simple to implement, yet it unlocks solutions to problems that would otherwise require nested loops.

---

## 2. How it Works

**Step 1 — Build the prefix sum array:**

Given array `A`, build `prefix` where `prefix[i]` = sum of `A[0..i]`.

```python
def build_prefix(A):
    prefix = [0] * (len(A) + 1)  # +1 for the "empty prefix" sentinel at index 0
    for i in range(len(A)):
        prefix[i + 1] = prefix[i] + A[i]
    return prefix
```

For `A = [3, 1, 4, 1, 5]`:

| i      | 0   | 1   | 2   | 3   | 4   | 5   |
| ------ | --- | --- | --- | --- | --- | --- |
| prefix | 0   | 3   | 4   | 8   | 9   | 14  |

**Step 2 — Answer range queries in O(1):**

The sum of `A[l..r]` (inclusive) is simply:

```
range_sum(l, r) = prefix[r + 1] - prefix[l]
```

For example, the sum of `A[1..3]` = `prefix[4] - prefix[1]` = `9 - 3` = **6** ✓ `(1 + 4 + 1)`

> 💡 The **+1 offset** (1-indexed prefix array) is the standard convention — it elegantly eliminates off-by-one edge cases and handles the empty prefix naturally.

---

## 3. How to Identify the Pattern

Look for these signals in the problem statement:

- 🔍 **"Sum of a subarray / range"** — any query asking for the sum between two indices
- 🔍 **"Number of subarrays with sum equal to k"** — a target sum condition on subarrays
- 🔍 **Multiple queries** on the same static array — preprocessing pays off
- 🔍 **"Running total"** or **"cumulative"** language in the problem
- 🔍 The problem involves **differences between two positions** (e.g., balance, net change)
- 🔍 A brute-force solution has **O(n²)** nested loops summing subarrays — prefix sum can optimize it to **O(n)**

---

## 4. Popular Sub-Patterns

### 4a. Prefix Sum + HashMap (Most Important!)

The most powerful combo. Store `prefix[i]` in a hashmap to find **how many previous prefixes satisfy a condition** in O(1).

**Classic use case — "Number of subarrays with sum = k":**

```python
def subarray_sum(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}  # prefix sum -> frequency

    for num in nums:
        prefix += num
        # If (prefix - k) was seen before, those subarrays sum to k
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1

    return count
```

The key insight: if `prefix[j] - prefix[i] = k`, then subarray `(i, j]` sums to `k`.

---

### 4b. 2D Prefix Sum

Extends the idea to matrices for **rectangle sum queries** in O(1).

```
prefix[i][j] = sum of all elements in the rectangle from (0,0) to (i-1, j-1)

rect_sum(r1,c1,r2,c2) = prefix[r2+1][c2+1]
                       - prefix[r1][c2+1]
                       - prefix[r2+1][c1]
                       + prefix[r1][c1]   ← add back the doubly-subtracted corner
```

---

### 4c. Prefix Sum on Difference Arrays

Used for **range update** problems — instead of updating every element in a range, mark only the endpoints. A single prefix sum pass at the end applies all updates in O(n).

```python
# Add `val` to all elements in range [l, r]
diff[l] += val
diff[r + 1] -= val
# Final array = prefix sum of diff[]
```

---

### 4d. Prefix XOR / Prefix Product

The same concept generalizes beyond addition:

- **Prefix XOR**: answers "XOR of subarray `[l, r]`" in O(1) — `xor[r] ^ xor[l-1]`
- **Prefix Product**: used in the classic _"Product of Array Except Self"_ problem

---

## 5. Practice Questions

### 🟢 Easy

| #   | Problem                                  | Key Idea                      |
| --- | ---------------------------------------- | ----------------------------- |
| 1   | **Range Sum Query - Immutable** (LC 303) | Direct prefix sum application |
| 2   | **Running Sum of 1D Array** (LC 1480)    | Build prefix in-place         |
| 3   | **Find Pivot Index** (LC 724)            | Left prefix == right suffix   |

### 🟡 Medium

| #   | Problem                                     | Key Idea                         |
| --- | ------------------------------------------- | -------------------------------- |
| 4   | **Subarray Sum Equals K** (LC 560)          | Prefix + HashMap                 |
| 5   | **Product of Array Except Self** (LC 238)   | Prefix & suffix products         |
| 6   | **Contiguous Array** (LC 525)               | Prefix + HashMap, treat 0s as -1 |
| 7   | **Range Sum Query 2D - Immutable** (LC 304) | 2D prefix sum                    |
| 8   | **Minimum Size Subarray Sum** (LC 209)      | Prefix + binary search           |
| 9   | **Corporate Flight Bookings** (LC 1109)     | Difference array                 |

### 🔴 Hard

| #   | Problem                                                 | Key Idea                          |
| --- | ------------------------------------------------------- | --------------------------------- |
| 10  | **Count of Range Sum** (LC 327)                         | Prefix + merge sort / sorted list |
| 11  | **Maximum Sum of 3 Non-Overlapping Subarrays** (LC 689) | Prefix windows + DP               |
| 12  | **Number of Subarrays with Bounded Maximum** (LC 795)   | Prefix counting                   |

---

> ✅ **Recommended order:** Start with LC 303 to understand the core, then LC 560 to master the Prefix + HashMap combo — that sub-pattern alone appears in dozens of medium/hard problems.
