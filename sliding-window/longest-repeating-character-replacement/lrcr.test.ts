import { characterReplacement } from './code';

describe('longest-repeating-character-replacement', () => {
	test('Case 0', () => {
		const s = 'AAAA';
		const k = 0;
		const output = 4;

		expect(characterReplacement(s, k)).toEqual(output);
	});

	test('Case 1', () => {
		const s = 'ABAB';
		const k = 2;
		const output = 4;

		expect(characterReplacement(s, k)).toEqual(output);
	});

	test('Case 2', () => {
		const s = 'AABABBA';
		const k = 1;
		const output = 4;

		expect(characterReplacement(s, k)).toEqual(output);
	});

	test('Case 3', () => {
		const s = '';
		const k = 1;
		const output = 0;

		expect(characterReplacement(s, k)).toEqual(output);
	});

	test('Case 4', () => {
		const s = 'ABCDEFG';
		const k = 2;
		const output = 3;

		expect(characterReplacement(s, k)).toEqual(output);
	});

	test('Case 5', () => {
		const s = 'ABA';
		const k = 0;
		const output = 1;

		expect(characterReplacement(s, k)).toEqual(output);
	});

	test('Case 6', () => {
		const s = 'AABABBB';
		const k = 2;
		const output = 6;

		expect(characterReplacement(s, k)).toEqual(output);
	});

	test('Case 7', () => {
		const s = 'BAAABBBB';
		const k = 2;
		const output = 6;

		expect(characterReplacement(s, k)).toEqual(output);
	});
});
