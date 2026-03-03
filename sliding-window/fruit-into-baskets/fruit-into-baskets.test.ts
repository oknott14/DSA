import { totalFruit } from './code';

describe('Fruit into baskets', () => {
	test('Case 1', () => {
		expect(totalFruit([1, 2, 2])).toEqual(3);
	});

	test('Case 2', () => {
		expect(totalFruit([0, 1, 2, 2])).toEqual(3);
	});

	test('Empty Arr', () => {
		expect(totalFruit([])).toEqual(0);
	});

	test('All Same', () => {
		expect(totalFruit([1, 1, 1, 1, 1])).toEqual(5);
	});

	test('Only Two', () => {
		expect(totalFruit([1, 2, 1, 2, 1, 2])).toEqual(6);
	});

	test('Split in middle', () => {
		expect(totalFruit([1, 2, 1, 2, 3, 1, 2])).toEqual(4);
		expect(totalFruit([1, 2, 3, 1, 2, 1, 2])).toEqual(4);
	});

	test('All different', () => {
		expect(totalFruit([1, 2, 3, 4, 5, 6, 7, 8, 9])).toEqual(2);
	});

	test('Case 3', () => {
		expect(totalFruit([0, 0, 1, 1])).toEqual(4);
	});
});
