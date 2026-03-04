// O(N) Runtime | O(1) Space
export function minSubArrayLen(target: number, nums: number[]): number {
	if (!nums.length) {
		// Empty array cant have sum
		return 0;
	}

	let left = 0;
	let currentTotal = 0;
	let shortest = nums.length + 1;

	for (let right = 0; right < nums.length; right++) {
		currentTotal += nums[right];

		while (currentTotal >= target) {
			shortest = Math.min(shortest, right - left + 1);
			currentTotal -= nums[left];
			left++;
		}

		if (shortest == 1) {
			return 1;
		}
	}

	if (shortest > nums.length) {
		shortest = 0;
	}

	return shortest;
}
