import { lengthOfLIS } from './code';

describe('longest-strictly-increasing-subsequence', () => {
	test('Counts increasing numbers in order', () => {
		const input = [1, 2, 3, 4];
		const output = 4;

		expect(lengthOfLIS(input)).toEqual(output);
	});

	test('Counts increasing numbers with skipping', () => {
		const input = [1, 2, 1, 3, 4];
		const output = 4;

		expect(lengthOfLIS(input)).toEqual(output);
	});

	test('Counts increasing numbers with many skips', () => {
		const input = [1, 2, 1, 3, 2, 4, 3, 5];
		const output = 5;

		expect(lengthOfLIS(input)).toEqual(output);
	});

	test('Can count from 2 separate sub sequences', () => {
		const input = [5, 6, 7, 1, 2, 3, 4];
		const output = 4;

		expect(lengthOfLIS(input)).toEqual(output);
	});

	test('Can count from 2 separate sub sequences when larger is longest', () => {
		const input = [5, 6, 7, 1, 2, 3, 4, 8, 9, 10];
		const output = 7;

		expect(lengthOfLIS(input)).toEqual(output);
	});

	test('Can count from two mixed subsequences', () => {
		const input = [5, 1, 6, 2, 7, 3, 8, 4, 9, 5, 10, 6, 7];
		const output = 7;

		expect(lengthOfLIS(input)).toEqual(output);
	});

	test('Case 1', () => {
		// **Input**: nums = [10,9,2,5,3,7,101,18]
		// **Output**: 4
		// **Explanation**: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

		const input = [10, 9, 2, 5, 3, 7, 101, 18];
		const output = 4;

		expect(lengthOfLIS(input)).toEqual(output);
	});

	test('Case 2', () => {
		const input = [0, 1, 0, 3, 2, 3];
		const output = 4; // 0 1 2 3

		expect(lengthOfLIS(input)).toEqual(output);
	});

	test('Case 3', () => {
		const input = [7, 7, 7, 7, 7, 7, 7];
		const output = 1;

		expect(lengthOfLIS(input)).toEqual(output);
	});

	test('Case 4', () => {
		const input: number[] = [];
		const output = 0;

		expect(lengthOfLIS(input)).toEqual(output);
	});
});
