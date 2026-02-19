export function twoSum(nums: number[], target: number): number[] {
	const map = new Map<number, number>();

	for (let idx = 0; idx < nums.length; idx++) {
		if (map.has(nums[idx])) {
			return [map.get(nums[idx])!, idx];
		}

		map.set(target - nums[idx], idx);
	}
	return [];
}

function enumerateNums(nums: number[]): Record<number, number> {
	return nums.reduce<Record<number, number>>((agg, num, index) => {
		agg[index] = num;
		return agg;
	}, {});
}

// Using Two Pointers
export function twoSumWith2Pointers(nums: number[], target: number): number[] {
	const idxToNums = enumerateNums(nums); // O(N) -> map indexes to number values
	const indexes = nums.map((_, idx) => idx); // O(N)
	indexes.sort((a, b) => idxToNums[a] - idxToNums[b]); //Sort indexes based on number map

	// Use two pointers to find index
	let left = 0;
	let right = nums.length - 1;

	while (left <= right) {
		if (nums[indexes[left]] + nums[indexes[right]] == target) {
			return [indexes[left], indexes[right]];
		} else if (nums[indexes[left]] + nums[indexes[right]] < target) {
			left++;
		} else {
			right--;
		}
	}

	return [];
}
