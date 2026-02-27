import { findAnagrams } from './code';

describe('Find all anagrams in string', () => {
	test('Case 1', () => {
		const s = 'bcaabccbaacb';
		const a = 'abc';

		expect(findAnagrams(s, a)).toEqual([0, 3, 6, 9]);
	});

	test.only('Case 2', () => {
		const s = 'baa';
		const a = 'aa';

		expect(findAnagrams(s, a)).toEqual([1]);
	});

	test('Has anagram with wrong letter in middle', () => {
		const s = 'abcba';
		const p = 'abab';

		expect(findAnagrams(s, p)).toEqual([]);
	});

	test('Anagram is longer than s', () => {
		const s = 'a';
		const p = 'ab';

		expect(findAnagrams(s, p)).toEqual([]);
	});

	test('Word has one short of anagram', () => {
		const s = 'ddabdd';
		const p = 'abc';

		expect(findAnagrams(s, p)).toEqual([]);
	});
});
