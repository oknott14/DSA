import { rotate } from './code';

describe('rotate-image', () => {
	function printMat(mat: number[][]): string {
		return mat.map((r) => r.join(' ')).join('\n');
	}

	test('Rotates even outer rows ', () => {
		const input = [
			[1, 2],
			[4, 3],
		];
		const output = [
			[4, 1],
			[3, 2],
		];

		expect(printMat(rotate(input))).toEqual(printMat(output));
	});

	test('Rotates odd 0 to col N', () => {
		const input = [
			[3, 4, 5],
			[2, 0, 0],
			[1, 0, 0],
		];
		const output = [
			[1, 2, 3],
			[0, 0, 4],
			[0, 0, 5],
		];

		expect(printMat(rotate(input))).toEqual(printMat(output));
	});

	test('Rotates even inner rows ', () => {
		const input = [
			[0, 0, 0, 0],
			[0, 1, 2, 0],
			[0, 4, 3, 0],
			[0, 0, 0, 0],
		];
		const output = [
			[0, 0, 0, 0],
			[0, 4, 1, 0],
			[0, 3, 2, 0],
			[0, 0, 0, 0],
		];

		expect(printMat(rotate(input))).toEqual(printMat(output));
	});

	test('Rotates odd inner rows ', () => {
		const input = [
			[0, 0, 0, 0, 0],
			[0, 1, 2, 3, 0],
			[0, 8, 0, 4, 0],
			[0, 7, 6, 5, 0],
			[0, 0, 0, 0, 0],
		];
		const output = [
			[0, 0, 0, 0, 0],
			[0, 7, 8, 1, 0],
			[0, 6, 0, 2, 0],
			[0, 5, 4, 3, 0],
			[0, 0, 0, 0, 0],
		];

		expect(printMat(rotate(input))).toEqual(printMat(output));
	});

	test('Case 1', () => {
		const input = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9],
		];
		const output = [
			[7, 4, 1],
			[8, 5, 2],
			[9, 6, 3],
		];

		expect(printMat(rotate(input))).toEqual(printMat(output));
	});

	test('Case 2', () => {
		const input = [
			[5, 1, 9, 11],
			[2, 4, 8, 10],
			[13, 3, 6, 7],
			[15, 14, 12, 16],
		];
		const output = [
			[15, 13, 2, 5],
			[14, 3, 4, 1],
			[12, 6, 8, 9],
			[16, 7, 10, 11],
		];

		expect(printMat(rotate(input))).toEqual(printMat(output));
	});
});
