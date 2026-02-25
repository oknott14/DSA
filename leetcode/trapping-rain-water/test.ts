import { trap } from './code';

describe('Trapping Rain Water', () => {
	test('Case 1', () => {
		expect(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])).toEqual(6);
	});

	test('Case 2', () => {
		expect(trap([4, 2, 0, 3, 2, 5])).toEqual(9);
	});

	test('Case 3', () => {
		expect(trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6])).toEqual(23);
	});

	test('All Increasing', () => {
		expect(trap([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1])).toEqual(
			0,
		);
	});
});
