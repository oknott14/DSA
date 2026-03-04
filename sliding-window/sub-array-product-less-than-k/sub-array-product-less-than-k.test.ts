import { numSubarrayProductLessThanK } from './code';

describe('Sub Array Product Less Than K', () => {
	test('Case 1', () => {
		expect(numSubarrayProductLessThanK([10, 5, 2, 6], 100)).toEqual(8);
	});

	test('K is less than all array elts', () => {
		expect(numSubarrayProductLessThanK([1, 2, 3, 4, 5, 6, 7, 8], 0)).toEqual(0);
	});

	test('separate sub arrs < k', () => {
		// 2 | 1 | 1 | 2 | 2 | 2 1 | 1 2 |
		expect(numSubarrayProductLessThanK([2, 1, 4, 1, 2, 2], 4)).toEqual(7);
	});
});
