/**
 * The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
 *
 * For example, for arr = [2,3,4], the median is 3.
 * For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
 * Implement the MedianFinder class:
 *
 * MedianFinder() initializes the MedianFinder object.
 * void addNum(int num) adds the integer num from the data stream to the data structure.
 * double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 *
 *
 * Example 1:
 * $1
 * Input
 * ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
 * [[], [1], [2], [], [3], []]
 * Output
 * [null, null, null, 1.5, null, 2.0]
 *
 * Explanation
 * MedianFinder medianFinder = new MedianFinder();
 * medianFinder.addNum(1);    // arr = [1]
 * medianFinder.addNum(2);    // arr = [1, 2]
 * medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
 * medianFinder.addNum(3);    // arr[1, 2, 3]
 * medianFinder.findMedian(); // return 2.0
 *
 *
 * Constraints:
 *
 * -105 <= num <= 105
 * There will be at least one element in the data structure before calling findMedian.
 * At most 5 * 104 calls will be made to addNum and findMedian.
 *
 *
 * Follow up:
 *
 * If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
 * If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
 */
import { HeapArray } from '../../TypeScript/data_structures/heaps/heap-array';

export class MedianFinder {
	min: HeapArray<number>;
	max: HeapArray<number>;

	constructor(size: number = 100) {
		this.min = new HeapArray<number>(size, (a, b) => a - b);
		this.max = new HeapArray<number>(size, (a, b) => b - a);
	}
	get size(): number {
		return this.min.size + this.max.size;
	}

	addNum(num: number) {
		if (this.max.size == 0) {
			// Add to Max if empty
			this.max.push(num);
		} else if (this.min.size < this.max.size) {
			// Add to min or rebalance if max is larger
			if (this.max.top! < num) {
				// num belongs in max -> put min of max in min and push num to max
				this.min.push(this.max.pop()!);
				this.max.push(num);
			} else {
				// Add to min
				this.min.push(num);
			}
		} else if (this.max.size < this.min.size) {
			// Min is larger than max -> put in max or rebalance
			if (num < this.min.top!) {
				// num belongs in min -> put max from min into max and push num into min
				this.max.push(this.min.pop()!);
				this.min.push(num);
			} else {
				// Add to max
				this.max.push(num);
			}
		} else if (num < this.min.top!) {
			// Equal size and num belongs in min
			this.max.push(this.min.pop()!);
			this.min.push(num);
		} else {
			// Equal size and num belongs in max
			this.max.push(num);
		}
	}

	findMedian(): number {
		if (this.size % 2 == 1) {
			return this.max.top!;
		} else {
			return (this.min.top! + this.max.top!) / 2;
		}
	}
}
