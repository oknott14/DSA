/**
 Do not return anything, modify nums in-place instead.
 */
export function moveZeroes(nums: number[]): void {
	let left = 0;
	let right = 1;
	let temp = 0;

	while (left < right && right < nums.length) {
		if (nums[left] != 0) {
			left++;

			if (left == right) {
				right++;
			}
		} else if (nums[right] == 0) {
			right++;
		} else {
			temp = nums[left];
			nums[left] = nums[right];
			nums[right] = temp;
			left++;
      right++;
		}
	}
}
