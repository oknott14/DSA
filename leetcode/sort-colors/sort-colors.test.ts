import { sortColors } from './code';

describe('Sort Colors', () => {
	test('Case 1', () => {
		const nums = [2, 0, 2, 1, 1, 0];
		sortColors(nums);

		expect(nums).toEqual([0, 0, 1, 1, 2, 2]);
	});

	test('Case 2', () => {
		const nums = [1, 0, 2];
		sortColors(nums);
		expect(nums).toEqual([0, 1, 2]);
	});

	test('Case 3', () => {
		const nums = [0, 2, 1];
		sortColors(nums);
		expect(nums).toEqual([0, 1, 2]);
	});

	test('Case 2 Elements', () => {
		const nums = [2, 1];
		sortColors(nums);
		expect(nums).toEqual([1, 2]);
	});

	test('Case All Same Number', () => {
		[0, 1, 2].forEach((num) => {
			const nums = new Array(20).fill(num);
			sortColors(nums);
			expect(nums).toBeDefined();
		});
	});

	test('Only 2 Numbers', () => {
		const arr = new Array<number>(100);

		for (let idx = 0; idx < arr.length; idx++) {
			arr[idx] = Math.random() > 0.5 ? 0 : 1;
		}

		sortColors(arr);

		const { numZeros, numOnes } = arr.reduce(
			(agg, curr) => {
				if (curr == 0) {
					agg.numZeros++;
				} else {
					agg.numOnes++;
				}

				return agg;
			},
			{ numZeros: 0, numOnes: 1 },
		);

		const ans = new Array(100);
		ans.fill(0, 0, numZeros);
		ans.fill(1, numZeros);

		expect(arr).toEqual(ans);
	});
});
