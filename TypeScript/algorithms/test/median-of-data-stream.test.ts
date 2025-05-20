import { randomInt } from 'crypto';
import { MedianFinder } from '../median-of-data-stream';

describe('median-of-data-stream', () => {
	describe('Min Max Heap MedianFinder', () => {
		test('addNum adds numbers and rebalances correctly', () => {
			const medianFinder = new MedianFinder();
			// [ 1 ]
			medianFinder.addNum(1);

			expect(medianFinder.max.top).toEqual(1);
			// [ 1 | 2 ]
			medianFinder.addNum(2);

			expect(medianFinder.max.top).toEqual(2);
			expect(medianFinder.min.top).toEqual(1);

			expect(medianFinder.size).toEqual(2);
			expect(medianFinder.size % 2).toEqual(0);

			// [ 1 | 2 | 3 ]
			medianFinder.addNum(3);

			expect(medianFinder.max.top).toEqual(2);

			// [ 0 1 | 2 3 ]
			medianFinder.addNum(0);
			// [ 0 1 | 1 | 2 3 ]
			medianFinder.addNum(1);
			// [ 0 0 1 | 1 2 3]
			medianFinder.addNum(0);

			expect(medianFinder.max.top).toEqual(1);
			expect(medianFinder.min.top).toEqual(1);
		});
	});

	test('Case 1', () => {
		const medianFinder = new MedianFinder();

		medianFinder.addNum(1);
		medianFinder.addNum(2);

		expect(medianFinder.findMedian()).toBeCloseTo(1.5, 3);

		medianFinder.addNum(3);

		expect(medianFinder.findMedian()).toEqual(2);
	});

	test('Case 2', () => {
		const medianFinder = new MedianFinder();

		medianFinder.addNum(1);
		medianFinder.addNum(2);
		medianFinder.addNum(3);
		medianFinder.addNum(10);
		medianFinder.addNum(4);
		medianFinder.addNum(6);
		medianFinder.addNum(9);
		medianFinder.addNum(8);
		medianFinder.addNum(5);
		medianFinder.addNum(7);

		expect(medianFinder.findMedian()).toEqual(5.5);
	});

	test('Case 3', () => {
		const medianFinder = new MedianFinder();
		medianFinder.addNum(-1);
		expect(medianFinder.findMedian()).toEqual(-1);
		medianFinder.addNum(-2);
		expect(medianFinder.findMedian()).toBeCloseTo(-1.5, 3);
		medianFinder.addNum(-3);
		expect(medianFinder.findMedian()).toEqual(-2);
		medianFinder.addNum(-4);
		expect(medianFinder.findMedian()).toBeCloseTo(-2.5, 3);
		medianFinder.addNum(-5);
		expect(medianFinder.findMedian()).toEqual(-3);
	});

	test('Case 4', () => {
		const medianFinder = new MedianFinder();
		medianFinder.addNum(1);
		expect(medianFinder.findMedian()).toEqual(1);
		medianFinder.addNum(2);
		expect(medianFinder.findMedian()).toBeCloseTo(1.5, 3);
		medianFinder.addNum(3);
		expect(medianFinder.findMedian()).toEqual(2);
		medianFinder.addNum(4);
		expect(medianFinder.findMedian()).toBeCloseTo(2.5, 3);
		medianFinder.addNum(5);
		expect(medianFinder.findMedian()).toEqual(3);
		medianFinder.addNum(6);
		expect(medianFinder.findMedian()).toBeCloseTo(3.5, 3);
		medianFinder.addNum(7);
		expect(medianFinder.findMedian()).toEqual(4);
		medianFinder.addNum(8);
		expect(medianFinder.findMedian()).toBeCloseTo(4.5, 3);
		medianFinder.addNum(9);
		expect(medianFinder.findMedian()).toEqual(5);
		medianFinder.addNum(10);
		expect(medianFinder.findMedian()).toBeCloseTo(5.5, 3);
	});

	test('Case 5', () => {
		const maxItems = 1000;
		const sortedArray = new Array<number>();

		const insert = (num: number) => {
			if (!sortedArray.length || sortedArray[sortedArray.length - 1] <= num) {
				sortedArray.push(num);
			} else if (num <= sortedArray[0]) {
				sortedArray.unshift(num);
			} else {
				let start = 0;
				let end = sortedArray.length - 1;
				let med: number = Math.floor((start + end) / 2);
				while (
					sortedArray[start] < num &&
					num < sortedArray[end] &&
					end - start > 1
				) {
					if (sortedArray[med] <= num) {
						start = med;
					} else {
						end = med;
					}

					med = Math.floor((start + end) / 2);
				}

				if (sortedArray[start] <= num) {
					sortedArray.splice(start + 1, 0, num);
				} else {
					sortedArray.splice(end + 1, 0, num);
				}
			}
		};

		const medianFinder = new MedianFinder();
		let median: number = 0;
		let toInsert: number = 0;
		for (let idx = 1; idx <= maxItems; idx++) {
			toInsert = randomInt(100);
			medianFinder.addNum(toInsert);
			insert(toInsert);

			if (idx % 2) {
				median = sortedArray[Math.floor(idx / 2)];
			} else {
				median = (sortedArray[idx / 2] + sortedArray[idx / 2 - 1]) / 2;
			}

			expect(medianFinder.max.top).toEqual(sortedArray[Math.floor(idx / 2)]);

			if (idx > 1) {
				expect(medianFinder.min.top).toEqual(
					sortedArray[Math.floor(idx / 2) - 1]
				);
			}
			expect(medianFinder.findMedian()).toBeCloseTo(median, 3);
		}
	});
});
