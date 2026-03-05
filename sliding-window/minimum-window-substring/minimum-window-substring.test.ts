import { minWindow } from './code';

describe('Minimum Window Sub String', () => {
	test('Case 1', () => {
		expect(minWindow('ADOBECODEBANC', 'ABC')).toEqual('BANC');
	});

	test('T is S', () => {
		expect(minWindow('a', 'a')).toEqual('a');
	});
});
