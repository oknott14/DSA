export function threeSumClosest(nums: number[], target: number): number {
	nums.sort((a, b) => a - b); // O(Log(N))

	const moveUntilDifferent = (idx: number, direction: number, end: number) => {
		idx += direction;

		while (idx != end && nums[idx] == nums[idx - direction]) {
			idx += direction;
		}

		return idx;
	};

	let curr = 0;
	let closest = nums[0] + nums[1] + nums[2];
	for (let anchor = 0; anchor < nums.length - 2; anchor++) {
		if (anchor > 0 && nums[anchor] == nums[anchor - 1]) continue;

		let left = anchor + 1;
		let right = nums.length - 1;

		while (left < right) {
			curr = nums[anchor] + nums[left] + nums[right];

			if (Math.abs(target - curr) < Math.abs(target - closest)) {
				closest = curr;
			}

			if (curr == target) {
				return target;
			} else if (curr < target) {
				left = moveUntilDifferent(left, 1, right);
			} else {
				right = moveUntilDifferent(right, -1, left);
			}
		}
	}

	return closest;
}
