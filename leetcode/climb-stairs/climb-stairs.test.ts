import { climbStairs } from './code';

describe('climb-stairs', () => {
	test('Base Case', () => {
		const n = 1;
		const output = 1;
		expect(climbStairs(n)).toEqual(output);
	});

	test('Case 1', () => {
		const n = 2;
		const output = 2;
		expect(climbStairs(n)).toEqual(output);
	});

	test('Case 2', () => {
		const n = 3;
		const output = 3;
		expect(climbStairs(n)).toEqual(output);
	});

	test('Case 4', () => {
		const n = 4;
		const output = 5;
		expect(climbStairs(n)).toEqual(output);
	});

	test('Case 4', () => {
		const n = 4;
		const output = 5;
		expect(climbStairs(n)).toEqual(output);
	});
});
