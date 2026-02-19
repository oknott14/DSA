import { removeDuplicates } from './code';

describe('Remove Duplicates', () => {
	test('Case 1', () => {
		const arr = [1, 1, 2];
		const soln = removeDuplicates(arr);

		expect(soln).toEqual(2);
		expect(arr.slice(0, 2)).toEqual([1, 2]);
	});

	test('Case 2', () => {
		const arr = [1, 1, 1];
		const soln = removeDuplicates(arr);

		expect(soln).toEqual(1);
		expect(arr.slice(0, 1)).toEqual([1]);
	});

	test('Case 3', () => {
		const arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5];
		const soln = removeDuplicates(arr);

		expect(soln).toEqual(5);
		expect(arr.slice(0, 5)).toEqual([1, 2, 3, 4, 5]);
	});
});
