import { coinChange } from './code';

describe('coin-change', () => {
	test('Base Case', () => {
		const input = [1];
		const amount = 1;
		const output = 1;
		expect(coinChange(input, amount)).toEqual(output);
	});

	test('Fails when sum < min(coins)', () => {
		expect(coinChange([2], 1)).toEqual(-1);
	});

	test('Can Sum 2 Denominations', () => {
		const input = [2, 1];
		const amount = 3;
		const output = 2;
		expect(coinChange(input, amount)).toEqual(output);
	});

	test('Can Sum 3 Denominations', () => {
		const input = [2, 3, 7];
		const amount = 12;
		const output = 3;
		expect(coinChange(input, amount)).toEqual(output);
	});

	test('Can Sum 1 denom many times', () => {
		const input = [3, 4, 7];
		expect(coinChange(input, 16)).toEqual(4);
		expect(coinChange(input, 9)).toEqual(3);
		expect(coinChange(input, 21)).toEqual(3);
	});

	test('Takes min when a + b = c', () => {
		const input = [3, 4, 7];
		const amount = 14;
		const output = 2;
		expect(coinChange(input, amount)).toEqual(output);
	});

	test('Case 1', () => {
		const input = [1, 2, 5];
		const amount = 11;
		const output = 3;
		expect(coinChange(input, amount)).toEqual(output);
	});

	test('Case 2', () => {
		const input = [2];
		const amount = 3;
		const output = -1;
		expect(coinChange(input, amount)).toEqual(output);
	});

	test('Case 3', () => {
		const input = [1];
		const amount = 0;
		const output = 0;
		expect(coinChange(input, amount)).toEqual(output);
	});

	test.only('Many', () => {
		const input = [13, 7, 5, 3, 2];
		const amount = 61;
		const output = 6;
		expect(coinChange(input, amount)).toEqual(output);
	});
});
