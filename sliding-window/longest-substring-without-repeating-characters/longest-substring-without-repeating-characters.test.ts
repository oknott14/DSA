import { lengthOfLongestSubstring } from './code';

describe('Longest substring without repeating characters', () => {
	test('Case 1', () => {
		expect(lengthOfLongestSubstring('abc')).toEqual(3);
	});

	test('Case 2', () => {
		expect(lengthOfLongestSubstring('aabcaa')).toEqual(3);
	});

	test('all same char', () => {
		expect(lengthOfLongestSubstring('aaaaaaaaaa')).toEqual(1);
	});

	test('Case 3', () => {
		expect(lengthOfLongestSubstring('abcacd')).toEqual(3);
	});

	test('Case 4', () => {
		expect(lengthOfLongestSubstring('abcabcabc')).toEqual(3);
	});

	test('Case 5', () => {
		expect(lengthOfLongestSubstring('abcdefa')).toEqual(6);
	});

	test('empty string', () => {
		expect(lengthOfLongestSubstring('')).toEqual(0);
	});

	test('single char', () => {
		expect(lengthOfLongestSubstring(' ')).toEqual(1);
	});

	test('Case 6', () => {
		expect(lengthOfLongestSubstring('pwwkew')).toEqual(3);
	});
});
