export function numSubarrayProductLessThanK(nums: number[], k: number): number {
	if (k == 0) {
		return 0;
	}

	let left = 0;
	let total = 0;
	let prod = 1;

	// If subarray length N has prod < k then all N-1 within have Prod < k
	for (let right = 0; right < nums.length; right++) {
		prod *= nums[right];

		while (k <= prod && left <= right) {
			//Shrink while prod is greater
			prod /= nums[left];
			left++;
		}

		total += right - left + 1;
	}

	return total;
}
