# Two Pointers

## 1. Overview

The Two Pointers pattern uses two index variables that traverse a data structure — typically an array or linked list — in a coordinated way to solve problems more efficiently than a brute-force nested loop approach. Instead of checking every pair of elements in O(n²), two pointers often reduce the solution to a single pass at **O(n) time** with **O(1) space**, making it one of the most powerful and elegant patterns in DSA.

---

## 2. How it Works

Two pointers are placed at strategic positions and moved according to some condition until they meet or cross. There are two primary configurations:

**Opposite Ends (Converging):** One pointer starts at the beginning, the other at the end. They move toward each other based on a comparison condition. Classic use case: finding a pair that sums to a target in a sorted array.

```
left, right = 0, len(arr) - 1
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        return [left, right]
    elif current_sum < target:
        left += 1
    else:
        right -= 1
```

**Same Direction (Fast & Slow / Sliding):** Both pointers start at the beginning but move at different speeds or under different conditions. Classic use case: removing duplicates in-place.

```
slow = 0
for fast in range(1, len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]
return slow + 1
```

---

## 3. How to Identify the Pattern

Look for these signals in a problem:

- The input is a **sorted array, string, or linked list** (or can be sorted without breaking the solution)
- The problem asks you to find a **pair, triplet, or subarray** satisfying some condition (sum, difference, target)
- The problem involves **in-place modification** — removing duplicates, partitioning, reversing
- The problem asks about **palindromes**, since you naturally compare from both ends
- The brute force is O(n²) nested loops and the problem constraints hint at needing something faster
- Keywords: _"pair", "two elements", "reverse in-place", "remove duplicates", "sorted array"_

---

## 4. Popular Sub-Patterns

**Converging Pointers** — Start at opposite ends, move inward. Used for pair-sum problems, palindrome checks, and container problems. Requires a sorted array or a structure where the comparison guides which pointer to move.

**Fast & Slow Pointers (Floyd's Algorithm)** — Two pointers move at different speeds through a linked list or array. The classic application is **cycle detection** in a linked list (slow moves 1 step, fast moves 2). Also used to find the middle of a linked list.

**Partition Pointers** — One pointer tracks a "boundary" while another scans forward. Used in problems like moving zeros to the end, separating even/odd numbers, or the partition step of QuickSort.

**Three Pointers** — An extension where one pointer is fixed (usually via an outer loop) and two pointers converge within the remaining subarray. The go-to technique for **3Sum** and similar k-sum problems.

**Sliding Window** — While often considered its own pattern, it is built on the same two-pointer foundation. A left and right pointer define a "window" that expands and contracts as it slides through the array. Best for subarray/substring problems.

---

## 5. Practice Questions

| Problem                             | Type               | Difficulty |
| ----------------------------------- | ------------------ | ---------- |
| Two Sum II (sorted array)           | Converging         | Easy       |
| Valid Palindrome                    | Converging         | Easy       |
| Reverse a String In-Place           | Converging         | Easy       |
| Remove Duplicates from Sorted Array | Partition          | Easy       |
| Move Zeroes                         | Partition          | Easy       |
| Linked List Cycle Detection         | Fast & Slow        | Easy       |
| Middle of the Linked List           | Fast & Slow        | Easy       |
| Container With Most Water           | Converging         | Medium     |
| 3Sum                                | Three Pointers     | Medium     |
| 3Sum Closest                        | Three Pointers     | Medium     |
| Sort Colors (Dutch National Flag)   | Partition (3 ptrs) | Medium     |
| Trapping Rain Water                 | Converging         | Hard       |
| Find the Duplicate Number           | Fast & Slow        | Medium     |

---

> **Key Insight:** Two pointers works because it makes a _greedy local decision_ at each step about which pointer to move, eliminating large swaths of search space. Always ask yourself: _"If I move this pointer, what am I definitively ruling out?"_
