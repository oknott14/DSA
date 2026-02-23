import { threeSum } from './code';

describe('3 Sum', () => {
	test('Case 1', () => {
		const nums = [-1, 0, 1, 2, -1, -4];
		const ans = [
			[-1, -1, 2],
			[-1, 0, 1],
		];

		const response = threeSum(nums);

		expect(ans.toString()).toEqual(response.toString());
	});

	test('Case 2', () => {
		const nums = [-1, -1, 0, 0, 1, 1];
		const ans = threeSum(nums);
		expect(ans.length).toEqual(1);
		expect(ans[0]).toEqual([-1, 0, 1]);
	});
});
