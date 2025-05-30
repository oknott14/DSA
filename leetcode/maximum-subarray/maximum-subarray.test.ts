import { maxSubArray } from './code';

describe('maximum-subarray', () => {
	test('sums all positive integers', () => {
		const input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
		const output = 55;

		expect(maxSubArray(input)).toEqual(output);
	});

	test('returns largest of all negatives', () => {
		const input = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10];
		const output = -1;

		expect(maxSubArray(input)).toEqual(output);
	});

	test('Sums positives before large negative', () => {
		const input = [2, 2, -10, 2];
		const output = 4;

		expect(maxSubArray(input)).toEqual(output);
	});

	test('Sums positives after large negative', () => {
		const input = [2, 1, -10, 2, 2];
		const output = 4;

		expect(maxSubArray(input)).toEqual(output);
	});

	test('Includes negative if sum of afterwards is larger', () => {
		const input = [1, 1, -3, 2, 2];
		const output = 4;

		expect(maxSubArray(input)).toEqual(output);
	});

	test('Case 1', () => {
		const input = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
		const output = 6;

		expect(maxSubArray(input)).toEqual(output);
	});

	test('Case 2', () => {
		const input = [1];
		const output = 1;

		expect(maxSubArray(input)).toEqual(output);
	});

	test('Case 3', () => {
		const input = [5, 4, -1, 7, 8];
		const output = 23;

		expect(maxSubArray(input)).toEqual(output);
	});
});
