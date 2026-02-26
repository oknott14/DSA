import { threeSumClosest } from './code';

describe('Three Sum Closest', () => {
	test('Case 1', () => {
		const nums = [-1, 2, 1, -4];
		const target = 1;
		const answer = 2;

		expect(threeSumClosest(nums, target)).toEqual(answer);
	});
});
