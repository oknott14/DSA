/**
 * A Generic Heap Implementation that stores the values of the Heap in an Array.
 */
export class HeapArray<Type> {
	private heap: Array<Type>;
	private currentSize: number = -1;

	constructor(
		/** The maximum number of values allowed in the heap. */
		private maxSize: number,
		/** Comparison function. Takes two values of type Type and compares them to eachother, returning a number.
		 * a < b => 1
		 * a = b => 0
		 * a > b => -1
		 */
		private compareTo: (a: Type, b: Type) => number
	) {
		if (this.maxSize <= 0) {
			throw new Error('maxSize must be larger than zero');
		}
	}

	get size(): number {
		return this.currentSize + 1;
	}

	get top(): null | Type {
		if (this.currentSize < 0) return null;
		return this.heap[this.currentSize];
	}

	private compare(a: number, b: number) {
		return this.compareTo(this.heap[a], this.heap[b]);
	}

	private swap(a: number, b: number) {
		let temp = this.heap[a];
		this.heap[a] = this.heap[b];
		this.heap[b] = temp;
	}
	push(value: Type): void {
		if (this.size == this.maxSize) {
			throw new Error('Failed to push value into Heap - max size reached');
		}
		if (this.currentSize < 0) {
			this.heap.push(value);
		} else {
			this.heap[++this.currentSize] = value;

			let pointer: number = this.currentSize;
			let parent: number;

			while (pointer > 0) {
				parent = Math.min((pointer - 1) / 2);

				if (this.compare(pointer, parent)) {
					this.swap(pointer, parent);
				} else {
					break;
				}

				pointer = parent;
			}
		}
	}
}
