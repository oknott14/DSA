/**
 Do not return anything, modify nums in-place instead.
 */
export function sortColors(nums: number[]): void {
	// 1, 0, 2, 0, 2, 1
	let left = 0; // First non zero elt
	let right = nums.length - 1; // First 2

	while (nums[left] == 0) {
		left++;
	}

	while (nums[right] == 2) {
		right--;
	}

	let middle = left; // End of 1s
	let temp = 0;
	while (middle <= right) {
		if (nums[middle] == 1) {
			middle++;
		} else if (nums[middle] == 0) {
			// Swap with left pos (first non zero) and increment left
			temp = nums[left];
			nums[left] = nums[middle];
			nums[middle] = temp;
			left++;
			middle = Math.max(left, middle);
		} else {
			// Swap with right pos (last non 2) and decrement right
			temp = nums[right];
			nums[right] = nums[middle];
			nums[middle] = temp;
			right--;
		}
	}
}
