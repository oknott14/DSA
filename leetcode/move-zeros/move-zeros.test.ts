import { moveZeroes } from './code';

describe('{testName}', () => {
	test('Case 1', () => {
		const arr = [0, 1, 0, 2, 0, 3, 0, 4];
		moveZeroes(arr);

		expect(arr).toEqual([1, 2, 3, 4, 0, 0, 0, 0]);
	});

	test('Case 2', () => {
		const arr = [2, 1];
		moveZeroes(arr);
		expect(arr).toEqual([2, 1]);
	});

	test('Case 3', () => {
		const arr = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0];
		moveZeroes(arr);
		expect(arr).toEqual([4, 2, 4, 3, 5, 1, 0, 0, 0, 0]);
	});
});
