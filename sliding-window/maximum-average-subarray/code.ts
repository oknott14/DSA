export function findMaxAverage(nums: number[], k: number): number {
	let idx;

	let maxSum = 0;
	for (idx = 0; idx < k; idx++) {
		maxSum += nums[idx];
	}

	let currSum = maxSum;
	while (idx < nums.length) {
		currSum -= nums[idx - k]; // Remove prev 1st elt
		currSum += nums[idx]; // Add new last elt

		maxSum = Math.max(currSum, maxSum);

		idx++;
	}

	return maxSum / k;
}
