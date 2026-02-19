export function removeDuplicates(nums: number[]): number {
	if (nums.length == 1) {
		return 1;
	} else if (nums.length == 2) {
		return nums[0] == nums[1] ? 1 : 2;
	}

	let left = 1;
	let right = 1;
	// 0 0 1 2 3 3 4 5
	while (right < nums.length) {
		if (nums[right] != nums[right - 1]) {
			nums[left] = nums[right];
			left++;
		}

		right++;
	}

	return left;
}
