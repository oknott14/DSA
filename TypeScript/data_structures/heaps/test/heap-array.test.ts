import { describe, expect, test } from '@jest/globals';
import { HeapArray } from '../heap-array';
import { randomInt } from 'crypto';
describe('Heap Array', () => {
	const maxItems = 100;
	const compareTo = (a: number, b: number) => a - b;

	class TestHeapArray extends HeapArray<number> {
		constructor() {
			super(maxItems, compareTo);
		}

		public getHeap() {
			return this.heap.slice(0, this.size);
		}
	}

	test('Can add a first item', async () => {
		const heap = new TestHeapArray();
		heap.push(1);
		expect(heap.getHeap()).toEqual([1]);
	});

	test('Swaps heap on push to maintain order', () => {
		const heap = new TestHeapArray();
		heap.push(1);
		heap.push(2);
		heap.push(3);

		expect(heap.getHeap()).toEqual([3, 1, 2]);

		heap.push(5);
		expect(heap.getHeap()).toEqual([5, 3, 2, 1]);

		heap.push(4);
		expect(heap.getHeap()).toEqual([5, 4, 2, 1, 3]);

		heap.push(10);
		heap.push(12);
		heap.push(6);
		heap.push(0);
		heap.push(3);

		expect(heap.getHeap()).toEqual([12, 6, 10, 4, 3, 2, 5, 1, 0, 3]);
	});

	test('pop removes item and correctly rebalances heap', () => {
		const heap = new TestHeapArray();
		heap.push(1);
		heap.push(2);
		heap.push(3);
		heap.push(5);

		expect(heap.pop()).toEqual(5);
		expect(heap.top).toEqual(3);
		expect(heap.getHeap()).toEqual([3, 1, 2]);

		heap.push(5);
		heap.push(4);

		expect(heap.pop()).toEqual(5);
		expect(heap.top).toEqual(4);
		expect(heap.getHeap()).toEqual([4, 3, 2, 1]);

		heap.push(10);
		heap.push(12);
		heap.push(6);
		heap.push(0);
		heap.push(3);

		expect(heap.pop()).toEqual(12);
		expect(heap.top).toEqual(10);
		expect(heap.getHeap()).toEqual([10, 4, 6, 3, 3, 2, 1, 0]);
	});

	test('always maintains the largest element at the top', () => {
		const heap = new TestHeapArray();
		let inserted = new Array<number>(maxItems);
		let max = 0;
		for (let idx = 0; idx < maxItems; idx++) {
			let toInsert = randomInt(100);
			inserted[idx] = toInsert;
			max = Math.max(max, toInsert);
			heap.push(toInsert);

			expect(heap.top).toEqual(max);
		}

		inserted = inserted.sort((a, b) => b - a);
		expect(inserted[0]).toEqual(max);

		for (let idx = 1; idx < maxItems; idx++) {
			expect(heap.pop()).toEqual(inserted[idx - 1]);
			expect(heap.top).toEqual(inserted[idx]);
		}

		expect(heap.pop()).toEqual(inserted[maxItems - 1]);
		expect(heap.size).toEqual(0);
	});
});
