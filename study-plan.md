# DSA Interview Prep — 3-Day Study Plan

---

## Day 1: Hashing · Linked Lists · Stacks & Queues

---

### Hashing

#### Overview

Hash maps and sets let you trade space for time, achieving O(1) average lookups. The core insight: precompute a map of what you've seen so future queries are instant. Almost any problem asking "have I seen X before?" or "how many times does X appear?" is a hashing candidate.

#### How to Recognize the Pattern

- Phrasing like "find two elements that...", "count frequency", or "group by property"
- You need O(1) lookup instead of an O(n) scan
- Detecting duplicates or tracking complements

#### Common Sub-Patterns

| Sub-pattern                 | Description                                                                                                |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Two Sum / complement lookup | Store seen values in a map. For each element, check if `target - element` exists. O(n) time.               |
| Frequency counting          | Count occurrences with a map, then answer queries about distribution (anagrams, top-K).                    |
| Grouping / bucketing        | Use a derived key (sorted string, tuple) to group items — Group Anagrams, isomorphic strings.              |
| Sliding window + hash       | Track window contents in a map, expand/shrink to maintain a constraint (Longest Substring Without Repeat). |

#### Practice Problems

| Problem                                        | Difficulty |
| ---------------------------------------------- | ---------- |
| Two Sum                                        | Easy       |
| Group Anagrams                                 | Medium     |
| Top K Frequent Elements                        | Medium     |
| Longest Substring Without Repeating Characters | Medium     |
| Subarray Sum Equals K                          | Medium     |
| Minimum Window Substring                       | Hard       |

---

### Linked Lists

#### Overview

Linked list problems are almost always about pointer manipulation. Master two techniques: the two-pointer (fast/slow) pattern and in-place reversal. Drawing diagrams before coding is non-negotiable — one misplaced pointer assignment causes infinite loops.

#### How to Recognize the Pattern

- In-place manipulation with O(1) space requirement
- "Detect a cycle", "find the middle", "reverse a portion"
- Merging or reordering two lists

#### Common Sub-Patterns

| Sub-pattern          | Description                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Fast & slow pointers | Two pointers at different speeds. Slow moves 1 step, fast moves 2. Used for cycle detection, finding the middle, and Nth-from-end. |
| In-place reversal    | Three-pointer technique (prev, curr, next) to reverse a list or sub-list iteratively in O(1) space.                                |
| Merge / sort         | Merge two sorted lists by comparing heads and stitching together. Foundation for merge sort on lists.                              |
| Dummy head trick     | Use a sentinel node before the head to simplify edge cases when the result list's head can change.                                 |

#### Practice Problems

| Problem                  | Difficulty |
| ------------------------ | ---------- |
| Reverse Linked List      | Easy       |
| Linked List Cycle        | Easy       |
| Merge Two Sorted Lists   | Easy       |
| Remove Nth Node From End | Medium     |
| Reorder List             | Medium     |
| Reverse Nodes in k-Group | Hard       |

---

### Stacks & Queues

#### Overview

Stacks handle LIFO problems — anything needing "the most recent unmatched thing". Queues (and deques) handle FIFO or sliding window extremes. Monotonic stacks are the key insight: maintain a stack that's always increasing or decreasing to answer span/histogram queries in O(n).

#### How to Recognize the Pattern

- Matching brackets, parentheses, or nested structures
- Next greater/smaller element queries
- Sliding window maximum/minimum

#### Common Sub-Patterns

| Sub-pattern                      | Description                                                                                                                                             |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monotonic stack                  | Pop elements that violate a monotone property. Each element pushed/popped once → O(n). Solves "next greater element", "largest rectangle in histogram". |
| Balanced parentheses             | Push open brackets, pop and verify on close. Works for any nested structure validation.                                                                 |
| Monotonic deque (sliding window) | Deque stores indices of useful candidates. Evict from front when out of window, from back when dominated. O(n) sliding window max/min.                  |
| BFS with queue                   | Level-order traversal of trees/graphs. Queue holds current frontier; process level by level.                                                            |

#### Practice Problems

| Problem                        | Difficulty |
| ------------------------------ | ---------- |
| Valid Parentheses              | Easy       |
| Min Stack                      | Medium     |
| Daily Temperatures             | Medium     |
| Decode String                  | Medium     |
| Largest Rectangle in Histogram | Hard       |
| Sliding Window Maximum         | Hard       |

---

## Day 2: Trees & Graphs · Heaps · Binary Search

---

### Trees & Graphs

#### Overview

Trees and graphs are traversal problems at heart. For trees: know DFS (recursive) and BFS (queue) cold. For graphs: add visited tracking. The key decision is always DFS vs BFS — DFS for path exploration and backtracking, BFS for shortest path in unweighted graphs.

#### How to Recognize the Pattern

- "Shortest path" → BFS first
- "All paths", "connected components", "cycle detection" → DFS
- Grid problems are implicit graphs (4-directional neighbors)

#### Common Sub-Patterns

| Sub-pattern                  | Description                                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Tree DFS (pre/in/post-order) | Recursive traversal. Pre: process node first. In: left→node→right (BST sorted order). Post: children before parent (subtree aggregation). |
| Tree BFS / level order       | Queue-based. Snapshot queue length at each level start to separate levels. Used for level averages, zigzag traversal.                     |
| Graph BFS (shortest path)    | Unweighted shortest path. Enqueue neighbors, mark visited on enqueue (not dequeue) to avoid re-queueing.                                  |
| Graph DFS / Union-Find       | Connected components, cycle detection, number of islands. Union-Find is faster for pure connectivity queries.                             |
| Topological sort             | Kahn's algorithm (BFS on in-degrees) or DFS post-order. For DAG ordering — course schedule, build dependencies.                           |
| Dijkstra / weighted graph    | Min-heap of (cost, node). Relax edges greedily. O((V+E) log V). Use when edge weights > 0.                                                |

#### Practice Problems

| Problem                               | Difficulty |
| ------------------------------------- | ---------- |
| Maximum Depth of Binary Tree          | Easy       |
| Number of Islands                     | Medium     |
| Binary Tree Level Order Traversal     | Medium     |
| Course Schedule                       | Medium     |
| Word Ladder                           | Hard       |
| Serialize and Deserialize Binary Tree | Hard       |

---

### Heaps

#### Overview

Heaps give you O(log n) insert and O(1) peek-at-extreme. The go-to structure for "K largest/smallest" problems and scheduling. Python has a min-heap by default — negate values for a max-heap. The two-heap pattern (one min, one max) maintains a running median.

#### How to Recognize the Pattern

- "K largest", "K smallest", "K most frequent"
- Merging K sorted lists or streams
- "Running median" or stream processing

#### Common Sub-Patterns

| Sub-pattern                 | Description                                                                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| K largest / K smallest      | Min-heap of size K for K largest (pop when size > K). O(n log K) — better than full sort when K << n.            |
| Two heaps (running median)  | Max-heap for lower half, min-heap for upper half. Balance sizes to keep medians at tops. O(log n) per insertion. |
| Merge K sorted lists        | Push head of each list into a min-heap. Pop min, push its next. O(n log K) where K = number of lists.            |
| Task scheduling / intervals | Heap tracks earliest finish time or next available slot. Used for Meeting Rooms II, Task Scheduler.              |

#### Practice Problems

| Problem                      | Difficulty |
| ---------------------------- | ---------- |
| Kth Largest Element in Array | Medium     |
| Top K Frequent Elements      | Medium     |
| Task Scheduler               | Medium     |
| Meeting Rooms II             | Medium     |
| Find Median from Data Stream | Hard       |
| Merge K Sorted Lists         | Hard       |

---

### Binary Search

#### Overview

Binary search isn't just for sorted arrays — it's a general "eliminate half the search space" technique. The key insight: if you can define a monotone predicate (false…false…true…true), you can binary search on it. Always be explicit about your invariant (`lo ≤ ans ≤ hi`) before coding.

#### How to Recognize the Pattern

- Sorted array or rotated sorted array
- "Minimum X such that condition holds" or "maximum X such that condition holds"
- The search space is a range of integers, not necessarily an array

#### Common Sub-Patterns

| Sub-pattern              | Description                                                                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Classic binary search    | `mid = lo + (hi - lo) // 2`. Update `lo = mid + 1` or `hi = mid - 1`. Know your termination condition (`lo ≤ hi` vs `lo < hi`).           |
| Left / right boundary    | Find first or last index where a condition holds. When target found, continue searching left (or right) instead of returning immediately. |
| Search on answer space   | Binary search on the answer itself (a number), not an array index. "Minimum eating speed", "Capacity to ship packages".                   |
| Rotated / modified array | Determine which half is sorted, then decide which half the target is in. Requires an extra condition check per iteration.                 |

#### Practice Problems

| Problem                              | Difficulty |
| ------------------------------------ | ---------- |
| Binary Search                        | Easy       |
| Search in Rotated Sorted Array       | Medium     |
| Find Minimum in Rotated Sorted Array | Medium     |
| Koko Eating Bananas                  | Medium     |
| Median of Two Sorted Arrays          | Hard       |
| Split Array Largest Sum              | Hard       |

---

## Day 3: Greedy · Backtracking · Dynamic Programming · Interview Skills

---

### Greedy

#### Overview

Greedy algorithms make the locally optimal choice at each step and hope it leads to a global optimum. The hard part is proving correctness — use an exchange argument (swapping two elements can't improve the solution) or a stays-ahead argument. If a greedy solution fails, the problem likely needs DP.

#### How to Recognize the Pattern

- Interval scheduling or activity selection
- Sorting by a greedy criterion enables a single scan
- "Minimum number of X to cover/achieve Y"

#### Common Sub-Patterns

| Sub-pattern          | Description                                                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Interval scheduling  | Sort by end time, greedily pick non-overlapping intervals. Classic greedy correctness proof by exchange argument.      |
| Jump game / coverage | Track the farthest reachable index. Greedily extend reach at each step. O(n), no sorting needed.                       |
| Two-pass greedy      | Solve left-to-right then right-to-left, combine results. Used for candy distribution and trapping rain water variants. |
| Greedy with sorting  | Sort array by a custom criterion, then scan once. E.g., sort meetings by start time, sort tasks by deadline.           |

#### Practice Problems

| Problem                   | Difficulty |
| ------------------------- | ---------- |
| Jump Game                 | Medium     |
| Jump Game II              | Medium     |
| Non-overlapping Intervals | Medium     |
| Gas Station               | Medium     |
| Partition Labels          | Medium     |
| Candy                     | Hard       |

---

### Backtracking

#### Overview

Backtracking = DFS on a decision tree, pruning branches that can't lead to valid solutions. The template is always the same: make a choice, recurse, undo the choice. State pruning is what separates an elegant solution from a TLE. Always think: what invalid branches can you cut early?

#### How to Recognize the Pattern

- "All combinations", "all permutations", "all subsets"
- "Find a valid arrangement" (N-Queens, Sudoku)
- Constraint satisfaction — explore possibilities and prune

#### Common Sub-Patterns

| Sub-pattern                    | Description                                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Subsets / combinations         | At each index, choose to include or exclude. For combinations of size K, prune when remaining elements can't fill K slots. |
| Permutations                   | Track a "used" set. At each position, try all unused elements. O(n!) leaf nodes before pruning.                            |
| Constraint propagation         | Sudoku, N-Queens. After each placement, immediately prune invalid positions. Key to making exponential search tractable.   |
| Palindrome / word partitioning | At each cut point, check if the prefix is valid (palindrome, dictionary word), recurse on suffix if so.                    |

#### Practice Problems

| Problem                 | Difficulty |
| ----------------------- | ---------- |
| Subsets                 | Medium     |
| Combination Sum         | Medium     |
| Permutations            | Medium     |
| Word Search             | Medium     |
| Palindrome Partitioning | Medium     |
| N-Queens                | Hard       |

---

### Dynamic Programming

#### Overview

DP = memoized recursion or bottom-up tabulation. The key is identifying overlapping subproblems and optimal substructure. Always define `dp[i]` clearly before coding. Start with the recurrence, then optimize space. Many DP problems have a 2D table that can be reduced to two 1D arrays.

#### How to Recognize the Pattern

- "Count ways to...", "minimum cost to...", "maximum value of..."
- A decision at each step affects future decisions
- The brute-force recursion has repeated subproblems (draw the recursion tree)

#### Common Sub-Patterns

| Sub-pattern                  | Description                                                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1D DP (linear)               | `dp[i]` depends on `dp[i-1]` or `dp[i-2]`. Fibonacci, climbing stairs, house robber. Often reducible to two variables.                |
| 2D DP (grid / strings)       | `dp[i][j]` derived from `dp[i-1][j]`, `dp[i][j-1]`, or `dp[i-1][j-1]`. LCS, edit distance, unique paths.                              |
| Knapsack (0/1 and unbounded) | 0/1: each item used once — iterate items outer, weights inner (forward). Unbounded: item can be reused — inner loop allows reuse.     |
| Interval DP                  | `dp[i][j]` = optimal solution for subarray `[i, j]`. Fill by increasing interval length. Burst Balloons, Matrix Chain Multiplication. |
| State machine DP             | Track multiple states (e.g., hold/not-hold stock). Define dp for each state, transition between them. Stock trading problems.         |
| DP on trees                  | Post-order DFS: compute dp for children before parent. Used for house robber on tree, max path sum.                                   |

#### Practice Problems

| Problem                             | Difficulty |
| ----------------------------------- | ---------- |
| Climbing Stairs                     | Easy       |
| Coin Change                         | Medium     |
| Longest Common Subsequence          | Medium     |
| Longest Increasing Subsequence      | Medium     |
| Edit Distance                       | Medium     |
| Best Time to Buy and Sell Stock III | Hard       |
| Burst Balloons                      | Hard       |

---

### Interviews & Tools

#### Overview

Technical skill accounts for roughly half of interview success. Communication, problem decomposition, and handling ambiguity account for the rest. Interviewers want to see how you think, not just what you know. Practice talking out loud while coding — silence is your biggest enemy.

#### How to Recognize When This Applies

- Every problem: clarify → example → approach → code → test
- Ask about constraints (size, sign, duplicates?) before writing a line
- Always announce your time and space complexity unprompted

#### Key Frameworks & Tools

| Framework            | Description                                                                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Problem-solving loop | 1) Clarify constraints and edge cases. 2) Work through 1–2 examples by hand. 3) State your approach and complexity. 4) Code. 5) Trace through your example. 6) Discuss optimizations.   |
| Complexity analysis  | State Big-O for time and space before your interviewer asks. For space: account for the recursion stack. For time: count how many times each element is touched.                        |
| Edge cases checklist | Empty input, single element, all same elements, negative numbers, integer overflow, circular structures, disconnected graphs.                                                           |
| Python cheat sheet   | `collections.defaultdict`, `collections.Counter`, `heapq` (min-heap; negate for max), `deque` for O(1) popleft, `bisect.bisect_left` for binary search.                                 |
| Stuck protocol       | Say "let me think about a simpler version first". Solve brute force, state its complexity, then optimize. A working O(n²) solution is worth more than a silent struggle for O(n log n). |

---

## Bonus: Quick-Reference Cheat Sheet

### Pattern → First Tool to Reach For

| Pattern                             | First instinct            |
| ----------------------------------- | ------------------------- |
| Count / lookup in O(1)              | Hash map                  |
| In-place list manipulation          | Two pointers / reversal   |
| Nested structure, "most recent"     | Stack                     |
| Shortest path, level order          | Queue (BFS)               |
| K largest / smallest                | Min-heap of size K        |
| Sorted input, "find X"              | Binary search             |
| Interval / scheduling               | Sort by end time (greedy) |
| All valid combinations              | Backtracking              |
| Repeated subproblems, optimal value | DP                        |
| Connected components                | Union-Find or DFS         |

### Complexity Quick-Reference

| Structure / Algorithm       | Time (average) | Space         |
| --------------------------- | -------------- | ------------- |
| Hash map insert / lookup    | O(1)           | O(n)          |
| Heap push / pop             | O(log n)       | O(n)          |
| Binary search               | O(log n)       | O(1)          |
| BFS / DFS on graph          | O(V + E)       | O(V)          |
| Backtracking (combinations) | O(2^n)         | O(n)          |
| Backtracking (permutations) | O(n!)          | O(n)          |
| DP (typical 1D)             | O(n)           | O(n) or O(1)  |
| DP (typical 2D)             | O(n²)          | O(n²) or O(n) |
| Merge sort / Heap sort      | O(n log n)     | O(n) / O(1)   |
| Dijkstra                    | O((V+E) log V) | O(V)          |
