/**
 * A Generic Heap Implementation that stores the values of the Heap in an Array.
 */
export class HeapArray<Type> {
	protected heap: Array<Type>;
	protected currentSize: number = -1;

	constructor(
		/** The maximum number of values allowed in the heap. */
		protected maxSize: number,
		/** Comparison function. Takes two values of type Type and compares them to eachother, returning a number.
		 * a < b => 1
		 * a = b => 0
		 * a > b => -1
		 */
		protected compareTo: (a: Type, b: Type) => number
	) {
		if (this.maxSize <= 0) {
			throw new Error('maxSize must be larger than zero');
		}

		this.heap = new Array<Type>(maxSize);
	}

	get size(): number {
		return this.currentSize + 1;
	}

	get top(): null | Type {
		if (this.currentSize < 0) return null;
		return this.heap[0];
	}

	protected compare(a: number, b: number) {
		return this.compareTo(this.heap[a], this.heap[b]);
	}

	protected swap(a: number, b: number) {
		let temp = this.heap[a];
		this.heap[a] = this.heap[b];
		this.heap[b] = temp;
	}

	protected parent(index: number) {
		return Math.floor((index - 1) / 2);
	}

	protected leftChild(index: number) {
		return 2 * index + 1;
	}

	protected rightChild(index: number) {
		return 2 * index + 2;
	}

	protected bubbleUp(index: number) {
		while (index > 0 && this.compare(index, this.parent(index)) >= 0) {
			this.swap(index, this.parent(index));
			index = this.parent(index);
		}
	}

	protected bubbleDown(index: number) {
		let max: number = index;

		while (index < this.currentSize) {
			if (
				this.leftChild(index) <= this.currentSize &&
				this.compare(index, this.leftChild(index)) < 0
			) {
				max = this.leftChild(index);
			}

			if (
				this.rightChild(index) <= this.currentSize &&
				this.compare(max, this.rightChild(index)) < 0
			) {
				max = this.rightChild(index);
			}

			if (max == index) {
				break;
			}

			this.swap(index, max);
			index = max;
		}
	}

	push(value: Type): void {
		this.heap[++this.currentSize] = value;
		this.bubbleUp(this.currentSize);
	}

	pop() {
		if (this.currentSize < 0) {
			return null;
		} else if (this.currentSize == 0) {
			return this.heap[this.currentSize--];
		} else {
			this.swap(0, this.currentSize--);
			this.bubbleDown(0);
		}

		return this.heap[this.currentSize + 1];
	}
}
