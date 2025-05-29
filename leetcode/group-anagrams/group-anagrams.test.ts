import { groupAnagrams } from './code';

describe('group-anagrams', () => {
	test('Does not group different words', () => {
		const input = ['a', 'b', 'c', 'd'];
		const output = [['a'], ['b'], ['c'], ['d']];

		expect(groupAnagrams(input)).toEqual(expect.arrayContaining(output));
	});

	test('Groups the same strings together', () => {
		const input = ['a', 'a', 'a'];
		const output = [['a', 'a', 'a']];

		expect(groupAnagrams(input)).toEqual(expect.arrayContaining(output));
	});

	test('Groups many of the same strings together', () => {
		const input = ['a', 'a', 'b', 'b'];
		const output = [
			['a', 'a'],
			['b', 'b'],
		];

		expect(groupAnagrams(input)).toEqual(expect.arrayContaining(output));
	});

	test('Groups anagrams', () => {
		const input = ['ab', 'ba'];
		const output = [['ab', 'ba']];

		expect(groupAnagrams(input)).toEqual(expect.arrayContaining(output));
	});

	test('groups many anagrams', () => {
		const input = ['ab', 'ba', 'bc', 'cb'];
		const output = [
			['ab', 'ba'],
			['bc', 'cb'],
		];

		expect(groupAnagrams(input)).toEqual(expect.arrayContaining(output));
	});

	test('does not group string that has N+ letters', () => {
		const input = ['ab', 'ba', 'bac'];
		const output = [['ab', 'ba'], ['bac']];

		expect(groupAnagrams(input)).toEqual(expect.arrayContaining(output));
	});

	test('Case 1', () => {
		const input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'];
		const output = [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']];

		expect(groupAnagrams(input)).toEqual(expect.arrayContaining(output));
	});

	test('Case 2', () => {
		const input = [''];
		const output = [['']];

		expect(groupAnagrams(input)).toEqual(expect.arrayContaining(output));
	});

	test('Case 3', () => {
		const input = ['a'];
		const output = [['a']];

		expect(groupAnagrams(input)).toEqual(expect.arrayContaining(output));
	});
});
