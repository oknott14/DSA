export function maxSubArray(nums: number[]): number {
	let max: number = nums[0];
	let sum: number = max;
	for (let idx = 1; idx < nums.length; idx++) {
		if (sum < 0) {
			sum = 0;
		}

		sum += nums[idx];
		max = Math.max(sum, max);
	}

	return Math.max(max, sum);
}
