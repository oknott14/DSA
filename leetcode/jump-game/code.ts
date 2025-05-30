export function canJump(nums: number[]): boolean {
	let end: number = nums.length - 1;
	let curr: number = end - 1;

	while (0 <= curr && 0 < end) {
		if (end <= curr + nums[curr]) {
			end = curr;
		}

		curr--;
	}

	return end == 0;
}
