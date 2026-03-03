export function longestOnes(nums: number[], k: number): number {
	let left = 0;
	let right = 0;
	let longest = 0;
	let flipped = 0;

	while (right < nums.length) {
		if (nums[right] == 0) {
			flipped++;
		}

		if (flipped <= k) {
			longest = Math.max(longest, right - left + 1);
		} else {
			if (nums[left] == 0) {
				flipped--;
			}
			left++;
		}
		right++;
	}

	return longest;
}
