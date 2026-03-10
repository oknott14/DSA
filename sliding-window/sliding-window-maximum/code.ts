export class MaxHeap {
	private heap: number[];
	private toDelete: Map<number, number> = new Map<number, number>();
	private size = 0;
	constructor(size: number) {
		this.heap = new Array(size);
	}

	private getParent(idx: number) {
		return Math.floor((idx - 1) / 2);
	}

	private getLeftChild(idx: number) {
		return idx * 2 + 1;
	}

	private getRightChild(idx: number) {
		return idx * 2 + 2;
	}

	private bubbleUp(idx: number) {
		let parent = this.getParent(idx);

		while (parent >= 0 && this.heap[parent] < this.heap[idx]) {
			let temp = this.heap[idx];
			this.heap[idx] = this.heap[parent];
			this.heap[parent] = temp;
			idx = parent;
			parent = this.getParent(idx);
		}
	}

	add(value: number): boolean {
		if (this.size >= this.heap.length) {
			return false;
		}

		this.heap[this.size] = value;
		this.bubbleUp(this.size++);
		this.checkAndPerformDeletion();
		return true;
	}

	private getLargestChild(idx: number): number {
		let left = this.getLeftChild(idx);
		let right = this.getRightChild(idx);

		if (left >= this.size && right >= this.size) {
			return -1; // Both are out of bounds
		} else if (left < this.size && right < this.size) {
			// Both are in bounds => return whichever has largest heap value
			return this.heap[left] < this.heap[right] ? right : left;
		} else {
			// One OB => return the other
			return left >= this.size ? right : left;
		}
	}

	private bubbleDown(idx: number) {
		let largestChild = this.getLargestChild(idx);
		let temp: number;
		while (1 <= largestChild) {
			// Swap with parent (max at top)
			temp = this.heap[largestChild];
			this.heap[largestChild] = this.heap[idx];
			this.heap[idx] = largestChild;
			// New parent is previous largest child
			idx = largestChild;
			largestChild = this.getLargestChild(idx);
		}
	}

	delete(item: number) {
		if (this.size == 0) {
			return false;
		}
		this.toDelete.set(item, (this.toDelete.get(item) ?? 0) + 1);
		this.checkAndPerformDeletion();
	}

	private checkAndPerformDeletion() {
		while (this.toDelete.has(this.max())) {
			this.pop();
		}
	}

	private pop() {
		if (this.size == 0) {
			throw new Error('No elements in heap');
		}

		let temp = this.heap[0];
		this.heap[0] = this.heap[--this.size];
		this.heap[this.size] = temp;
		this.bubbleDown(0);

		if (this.toDelete.has(this.heap[this.size])) {
			this.toDelete.set(
				this.heap[this.size],
				this.toDelete.get(this.heap[this.size])! - 1,
			);

			if (this.toDelete.get(this.heap[this.size]) == 0) {
				this.toDelete.delete(this.heap[this.size]);
			}
		}
		return this.heap[this.size];
	}

	max() {
		if (this.size > 0) {
			return this.heap[0];
		} else {
			throw new Error('No elements');
		}
	}
}
export function maxSlidingWindow(nums: number[], k: number): number[] {
	const heap = new MaxHeap(k);

	for (let idx = 0; idx < k && idx < nums.length; idx++) {
		heap.add(nums[idx]);
	}

	const results = [heap.max()];

	// Find max quickly
	// Find any number quickly
	for (let idx = k; idx < nums.length; idx++) {
		heap.delete(nums[idx - k]); // O(log(k)) amortized
		heap.add(nums[idx]); // O(log(K))
		results.push(heap.max()); // O(1)
	}
	return results;
}
