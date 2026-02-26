# Solution

## Pre-Requisites

1. The list is sorted (by index if list cannot be modified)

## Algorithm

First initialize a left pointer at the zero position of the array. This will be the smallest number in the sorted array.

Next, initialize a right pointer at the last position in the array. This is the largest number in the array.

The algorithm behaves by moving the pointers closer together and attempting to shrink the difference between the sum of `nums[left]` and `nums[right]`

Consider `nums = [-2, -1, 0, 3, 5, 7]` and `target = 4`.

The first iteration has `nums[left] + nums[right] = 5`. Since the sum is larger than the target, we need to decrease the sum. With `nums[left]` being the minimum of the array, the only way to do this is to decrease the right pointer.

The second iteration now has `right = 4` and `nums[left] + nums[right] = 3`. Following the same logic, the only way to increase the sum is to increase the left pointer.

| Iteration | Left | Right | Sum | Comparison     |
| --------- | ---- | ----- | --- | -------------- |
| 0         | 0    | 5     | 5   | `sum < target` |
| 1         | 0    | 4     | 3   | `sum < target` |
| 2         | 1    | 4     | 4   | `sum = target` |

The algorithm continues unti either `left == right` or `nums[left] + nums[right] == target`.
