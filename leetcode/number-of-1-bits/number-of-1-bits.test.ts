import { hammingWeight } from './code';

describe('number-of-1-bits', () => {
	test('Base Case 1', () => {
		const input = 1;
		const output = 1;
		expect(hammingWeight(input)).toEqual(output);
	});

	test('Base Case 0', () => {
		const input = 0;
		const output = 0;
		expect(hammingWeight(input)).toEqual(output);
	});

	test('Case 1', () => {
		const input = 11;
		const output = 3;
		expect(hammingWeight(input)).toEqual(output);
	});

	test('Case 2', () => {
		const input = 128;
		const output = 1;
		expect(hammingWeight(input)).toEqual(output);
	});

	test('Case 3', () => {
		const input = 2147483645;
		const output = 30;
		expect(hammingWeight(input)).toEqual(output);
	});
});
