# Sliding Window

## 1. Overview

The Sliding Window pattern maintains a contiguous "window" — a subarray or substring — that expands and contracts as it moves through the data. Rather than recomputing results from scratch for every possible subarray (O(n²) or O(n³) brute force), the window carries state incrementally, adding one element as it grows and dropping one as it shrinks. This reduces most problems to a single linear pass at **O(n) time** and typically **O(1) or O(k) space**, where k is the size of your character set or window constraint.

It is one of the most frequently tested patterns in interviews, appearing heavily in subarray and substring problems.

---

## 2. How it Works

There are two main flavors of window, but both share the same core loop structure: a `right` pointer expands the window each iteration, and a `left` pointer shrinks it when some condition is violated.

**Fixed-Size Window** — The window size `k` is given. Slide it across the array, adding the new right element and dropping the old left element each step.

```python
# Maximum sum subarray of size k
window_sum = sum(arr[:k])
max_sum = window_sum

for right in range(k, len(arr)):
    window_sum += arr[right] - arr[right - k]  # add new, drop old
    max_sum = max(max_sum, window_sum)

return max_sum
```

**Variable-Size Window** — The window grows until a constraint is violated, then the left pointer advances to restore validity. The answer is tracked throughout.

```python
# Longest substring without repeating characters
seen = {}
left = 0
max_len = 0

for right in range(len(s)):
    if s[right] in seen and seen[s[right]] >= left:
        left = seen[s[right]] + 1   # shrink: move left past the duplicate
    seen[s[right]] = right
    max_len = max(max_len, right - left + 1)

return max_len
```

The key insight in both cases is that **you never need to recompute the entire window** — you only process the element entering and the element leaving.

---

## 3. How to Identify the Pattern

Look for these signals:

- The problem involves a **contiguous subarray or substring** — non-contiguous problems don't fit this pattern
- The problem asks for an **optimal subarray** — longest, shortest, maximum sum, minimum length
- There is a **constraint that defines window validity** — at most k distinct characters, sum ≤ target, no repeating elements
- The brute force involves **nested loops scanning subarrays**, hinting that a smarter linear scan exists
- Keywords: _"subarray", "substring", "contiguous", "window", "at most k", "longest", "shortest", "minimum length"_

**Watch out:** If the array is unsorted and the problem asks for non-contiguous elements, Two Pointers or DP is likely a better fit than Sliding Window.

---

## 4. Popular Sub-Patterns

**Fixed-Size Window** — Window size `k` is explicitly given. Maintain a running aggregate (sum, max, frequency map) and shift the window one step at a time. The drop-and-add step is the key mechanic. Used in: maximum sum subarray of size k, finding all anagrams of a string.

**Variable-Size Window (Expand & Shrink)** — No fixed size; the window grows as long as the constraint holds and shrinks from the left when violated. The two common variants are:

- _Maximize the window_ — track the longest valid window seen (e.g. longest substring with at most k distinct characters)
- _Minimize the window_ — shrink aggressively once valid, record the shortest (e.g. minimum window substring)

**Sliding Window + HashMap/Frequency Map** — The constraint involves character or element frequencies (e.g. "at most 2 distinct characters", "contains all characters of pattern T"). A frequency map tracks the window's composition and a counter tracks how many requirements are currently satisfied. This is the engine behind many hard sliding window problems.

**Sliding Window + Monotonic Deque** — When you need the **maximum or minimum within the current window** at every step, a simple running variable isn't enough since elements leaving the window may have been the max. A monotonic deque maintains a decreasing (or increasing) sequence of candidates, giving O(1) window-max queries. Used in: Sliding Window Maximum.

**Shrinkable vs Non-Shrinkable Windows** — A subtle but useful distinction. In some problems (find longest valid window) you never shrink the window below its current maximum size — `left` only advances when `right` does. This guarantees the window size is monotonically non-decreasing and simplifies the logic.

---

## 5. Practice Questions

| Problem                                              | Sub-Pattern                | Difficulty |
| ---------------------------------------------------- | -------------------------- | ---------- |
| Maximum Average Subarray I                           | Fixed Window               | Easy       |
| Contains Duplicate II                                | Fixed Window               | Easy       |
| Find All Anagrams in a String                        | Fixed Window + Freq Map    | Medium     |
| Longest Substring Without Repeating Characters       | Variable Window            | Medium     |
| Longest Repeating Character Replacement              | Variable Window            | Medium     |
| Max Consecutive Ones III                             | Variable Window            | Medium     |
| Fruit Into Baskets                                   | Variable Window + HashMap  | Medium     |
| Longest Substring with At Most K Distinct Characters | Variable Window + HashMap  | Medium     |
| Minimum Size Subarray Sum                            | Variable Window (minimize) | Medium     |
| Subarray Product Less Than K                         | Variable Window            | Medium     |
| Minimum Window Substring                             | Variable Window + Freq Map | Hard       |
| Sliding Window Maximum                               | Window + Monotonic Deque   | Hard       |
| Substring with Concatenation of All Words            | Fixed Window + HashMap     | Hard       |

---

> **Key Insight:** The window always represents the **best candidate you're currently evaluating**. The art of sliding window is defining exactly what makes a window _valid_ and knowing whether to expand, shrink, or record based on that validity check. Get that condition crystal clear before writing any code.
