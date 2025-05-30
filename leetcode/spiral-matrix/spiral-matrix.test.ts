import { spiralOrder } from './code';

describe('spiral-matrix', () => {
	test('Spirals Odd Base Case', () => {
		const input: number[][] = [[1]];

		const output: number[] = [1];

		expect(spiralOrder(input)).toEqual(output);
	});

	test('Spirals Even Base Case', () => {
		const input: number[][] = [
			[1, 2],
			[4, 3],
		];

		const output: number[] = [1, 2, 3, 4];

		expect(spiralOrder(input)).toEqual(output);
	});

	test('Spirals M != N Base Case', () => {
		const input: number[][] = [[1, 2]];

		const output: number[] = [1, 2];

		expect(spiralOrder(input)).toEqual(output);
	});

	test('Spirals larger odd M = N', () => {
		const input: number[][] = [
			[1, 2, 3, 4, 5],
			[16, 17, 18, 19, 6],
			[15, 24, 25, 20, 7],
			[14, 23, 22, 21, 8],
			[13, 12, 11, 10, 9],
		];

		const output: number[] = [
			1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
			22, 23, 24, 25,
		];

		expect(spiralOrder(input)).toEqual(output);
	});

	test('Spirals large even M = N', () => {
		const input: number[][] = [
			[0, 1, 2, 3],
			[11, 12, 13, 4],
			[10, 15, 14, 5],
			[9, 8, 7, 6],
		];

		const output: number[] = [
			0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
		];

		expect(spiralOrder(input)).toEqual(output);
	});

	test('Spirals larger odd M != N', () => {
		const input: number[][] = [
			[1, 2, 3, 4, 5, 6, 7],
			[18, 19, 20, 21, 22, 23, 8],
			[17, 28, 27, 26, 25, 24, 9],
			[16, 15, 14, 13, 12, 11, 10],
		];

		const output: number[] = [
			1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
			22, 23, 24, 25, 26, 27, 28,
		];

		expect(spiralOrder(input)).toEqual(output);
	});

	test('Spirals larger even M != N', () => {
		const input: number[][] = [
			[1, 2, 3, 4, 5, 6],
			[18, 19, 20, 21, 22, 7],
			[17, 28, 29, 30, 23, 8],
			[16, 27, 26, 25, 24, 9],
			[15, 14, 13, 12, 11, 10],
		];

		const output: number[] = [
			1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
			22, 23, 24, 25, 26, 27, 28, 29, 30,
		];

		expect(spiralOrder(input)).toEqual(output);
	});

	test('Case 1', () => {
		const input: number[][] = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9],
		];

		const output: number[] = [1, 2, 3, 6, 9, 8, 7, 4, 5];

		expect(spiralOrder(input)).toEqual(output);
	});

	test('Case 2', () => {
		const input: number[][] = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
		];

		const output: number[] = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7];

		expect(spiralOrder(input)).toEqual(output);
	});
});
