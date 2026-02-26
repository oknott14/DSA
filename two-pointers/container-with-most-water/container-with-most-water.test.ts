import { maxArea } from './code';

describe('Container With Most Water', () => {
	test('Case 1', () => {
		const height = [1, 8, 6, 2, 5, 4, 8, 3, 7];

		expect(maxArea(height)).toEqual(49);
	});

	test('Case 2', () => {
		expect(maxArea([1, 1])).toEqual(1);
	});

	test('Case 3', () => {
		expect(maxArea([0, 0])).toEqual(0);
		expect(maxArea([0, 1])).toEqual(0);
	});

	test('Case 4', () => {
		const height = [1, 3, 1, 1, 100, 100, 1, 2, 15, 3];
		expect(maxArea(height)).toEqual(100);
	});

	test('Case 5', () => {
		const height = [10, 8, 7, 6, 5, 10, 4, 6]
	})
});
