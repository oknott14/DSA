export function maxSlidingWindow(nums: number[], k: number): number[] {
	if (k == 0 || nums.length == 0) {
		return [];
	}

	const dq = [];

	for (let idx = 0; idx < Math.min(nums.length, k); idx++) {
		while (dq.length > 0 && nums[dq[dq.length - 1]] <= nums[idx]) {
			dq.pop();
		}

		dq.push(idx);
	}

	const results = [nums[dq[0]]];

	for (let idx = k; idx < nums.length; idx++) {
		while (dq[0] < idx - k) {
			dq.shift();
		}

		while (dq.length > 0 && nums[dq[dq.length - 1]] <= nums[idx]) {
			dq.pop();
		}

		dq.push(idx);

		results.push(nums[dq[0]]);
	}

	return results;
}
