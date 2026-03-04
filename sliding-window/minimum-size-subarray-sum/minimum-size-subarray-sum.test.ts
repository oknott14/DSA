import { minSubArrayLen } from './code';

describe('Minimum Size Subarray Sum', () => {
	test('Has Target', () => {
		expect(minSubArrayLen(4, [1, 2, 3, 4])).toEqual(1);
	});

	test('Has larger than target', () => {
		expect(minSubArrayLen(1, [0, 0, 0, 0, 2, 0, 0])).toEqual(1);
	});

	test('Selects smallest', () => {
		expect(minSubArrayLen(5, [1, 2, 2, 0, 1, 4, 0, 3, 3])).toEqual(2);
	});

	test('No Sum', () => {
		expect(minSubArrayLen(100, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])).toEqual(0);
	});

	test('Empty arr', () => {
		expect(minSubArrayLen(100, [])).toEqual(0);
	});

	test('Sum is array length', () => {
		expect(minSubArrayLen(15, [1, 2, 3, 4, 5])).toEqual(5);
	});
});
