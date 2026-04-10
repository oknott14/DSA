# Notes

### Goal

- Find the max of K elements in O(1) time
- Be able to remove / insert elementes efficiently

### Brute Force

Loop over K elements each iteration. Runtime is O(N * (N - K)) (really less)

### Optimizations

1. Max Heap ( O(N^2) )
  - O(1) max retrieval
  - O(log(N)) insertion
  - O(N) worst case deletion

2. Balanced BST ( O(N * log(N)) )
  - O(log(N)) max retrieval
  - O(log(N)) insertion
  - O(log(N)) deletion

3. Sorted List ( O(N * log(N)) )
  - O(1) max retrieval
  - O(log(N)) insertion
  - O(log(N)) deletion

4. Linked List with Map ( O(N^2) )
  - O(1) max retrieval
  - O(N) insertion
  - O(1) deletion

5. Max Heap with Lazy Deletion
  - O(1) max retrieval
  - O(Log(N)) insertion
  - O(Log(N)) amortized deletion
