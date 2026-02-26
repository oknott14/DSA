import { findMaxAverage } from './code';

describe('Maximum Average Subarray 1', () => {
	test('Case 1', () => {
		expect(findMaxAverage([1, 12, -5, -6, 50, 3], 4)).toEqual(12.75);
	});
});
