import { maxSlidingWindow } from './code';

describe('Sliding Window Maximum', () => {
	test.only('Case 1', () => {
		expect(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)).toEqual([
			3, 3, 5, 5, 6, 7,
		]);
	});

	test('Single Element', () => {
		expect(maxSlidingWindow([1], 1)).toEqual([1]);
		expect(maxSlidingWindow([1], 100)).toEqual([1]);
	});

	test('K larger than nums', () => {
		expect(maxSlidingWindow([1, 4, 3, 2, 5, 8, 6, 7, 9, 1], 100)).toEqual([9]);
	});

	test('K is Zero', () => {
		expect(maxSlidingWindow([1, 233, 4, 5, 6, 7, 8, 9], 0)).toEqual([]);
	});

	test('K is 1/2 nums', () => {
		expect(maxSlidingWindow([2, 1, 2, 3], 2)).toEqual([2, 2, 3]);
	});
});
