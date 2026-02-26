export function containsNearbyDuplicate(nums: number[], k: number): boolean {
	const kSet = new Set();

	let idx = 0;

	for (idx = 0; idx < k && idx < nums.length; idx++) {
		if (kSet.has(nums[idx])) {
			return true;
		}

		kSet.add(nums[idx]);
	}

	for (idx = k; idx < nums.length; idx++) {
		if (kSet.has(nums[idx])) {
			return true;
		}

		kSet.add(nums[idx]);
		kSet.delete(nums[idx - k]);
	}

	return false;
}
