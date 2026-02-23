// Time Complexity: O(N^2)
// Space Complexity: O(1) ?? O(N/3) counting solns array
export function threeSum(nums: number[]): number[][] {
	const solns: number[][] = [];
	let curr = 0;
	nums.sort((a, b) => a - b);

	const moveUntilDifferent = (idx: number, direction: number, end: number) => {
		idx += direction;
		while (idx != end && nums[idx] == nums[idx - direction]) {
			idx += direction;
		}

		return idx;
	};

	for (let anchor = 0; anchor < nums.length - 2; anchor++) {
		if (anchor > 0 && nums[anchor] == nums[anchor - 1]) continue;

		let left = anchor + 1;
		let right = nums.length - 1;

		while (left < right) {
			curr = nums[anchor] + nums[left] + nums[right];

			if (curr == 0) {
				solns.push([nums[anchor], nums[left], nums[right]]);
				right--;
				left = moveUntilDifferent(left, 1, right);
			} else if (curr < 0) {
				left = moveUntilDifferent(left, 1, right);
			} else {
				right = moveUntilDifferent(right, -1, left);
			}
		}
	}

	return solns;
}
/*// O(N ^ 2)+ Time Complexity
// O(N) Space Complexity
export function threeSum(nums: number[]): number[][] {
	const soln: number[][] = [];
	const residuals = new Map<number, number>();
	const used = new Set<string>();
	// a + b + c = 0
	// target = b + c
	let anchor = 0;
	let target = 0;

	while (anchor < nums.length - 2) {
		residuals.clear();
		target = 0 - nums[anchor];

		for (let idx = anchor + 1; idx < nums.length; idx++) {
			if (residuals.has(nums[idx])) {
				const sol = [nums[anchor], nums[residuals.get(nums[idx])!], nums[idx]];
				sol.sort((a, b) => a - b);

				if (!used.has(sol.toString())) {
					soln.push(sol);
					used.add(sol.toString());
				}

				residuals.delete(nums[idx]);
			} else {
				residuals.set(target - nums[idx], idx);
			}
		}

		anchor++;
	}

	return soln;
}
*/
