import { reverseBits } from './code';

describe('reverse-bits', () => {
	test('Case 1', () => {
		const input = 43261596;
		const output = 964176192;
		expect(reverseBits(input)).toEqual(output);
	});

	test('Case 2', () => {
		const input = 4294967293;
		const output = 3221225471;
		expect(reverseBits(input)).toEqual(output);
	});
});
