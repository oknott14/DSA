import { twoSum } from './code';
describe('Two Sum', () => {
	test('Case 1', () => {
		const arr = [2, 7, 11, 15];
		const target = 9;

		const result = twoSum(arr, target);

		expect(result).toEqual([0, 1]);
	});

	test('Case 2', () => {
		const nums = [3, 2, 4];
		const target = 6;

		const result = twoSum(nums, target);
		expect(result).toEqual([1, 2]);
	});

	test('Case 3', () => {
		const nums = [3, 3];
		const target = 6;
		const result = twoSum(nums, target);
		expect(result).toEqual([0, 1]);
	});
});
