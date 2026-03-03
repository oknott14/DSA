import { longestOnes } from './code';

describe('Max Consecutive Ones 3', () => {
	test('Empty Arr', () => {
		expect(longestOnes([], 1)).toEqual(0);
	});

	test('K is Zero', () => {
		expect(longestOnes([1, 1, 0, 1], 0)).toEqual(2);
	});

	test('All zeros', () => {
		expect(longestOnes([0, 0, 0], 2)).toEqual(2);
	});

	test('Flips in the middle', () => {
		expect(longestOnes([1, 1, 0, 1, 1], 1)).toEqual(5);
	});

	test('Flips preceding', () => {
		expect(longestOnes([0, 1, 1], 1)).toEqual(3);
	});

	test('Flips following', () => {
		expect(longestOnes([1, 1, 0], 1)).toEqual(3);
	});

	test('Flips many', () => {
		expect(longestOnes([0, 1, 1, 0, 1, 1, 0], 3)).toEqual(7);
	});

	test('Selects longest ones', () => {
		expect(longestOnes([1, 0, 1, 0, 1, 1, 1], 1)).toEqual(5);
	});
});
