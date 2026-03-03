import { characterReplacement } from './code';

describe('Longest Repeating Character Replacement', () => {
	test('Case 1', () => {
		expect(characterReplacement('aabaa', 1)).toEqual(5);
	});

	test('empty string', () => {
		expect(characterReplacement('', 100)).toEqual(0);
	});

	test('same char', () => {
		expect(characterReplacement('aaaaaa', 1)).toEqual(6);
	});

	test('zero replacement', () => {
		expect(characterReplacement('aaabbabb', 0)).toEqual(3);
	});

	test('replacement switches', () => {
		expect(characterReplacement('bbaaaa', 2)).toEqual(6);
	});
});
