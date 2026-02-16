import { removeDuplicates } from './code';

describe('Remove Duplicates from Sorted List', () => {
	test('Case 1', () => {
		const arr = [1, 1, 1, 2, 3, 3];
		const result = removeDuplicates(arr);

		expect(result).toBe(5);

		new Array(1, 1, 2, 3, 3).forEach((val, idx) => {
			expect(arr[idx]).toEqual(val);
		});
	});
});
