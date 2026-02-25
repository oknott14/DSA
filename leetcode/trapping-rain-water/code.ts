export function trap(height: number[]): number {
	let total = 0;

	let left = 0;
	let maxLeft = left;
	let right = height.length - 1;
	let maxRight = right;

	while (left <= right) {
		if (height[maxLeft] <= height[maxRight]) {
			// If we are undef the max height => add vertical diff
			if (height[left] < height[maxLeft]) {
				total += height[maxLeft] - height[left];
			} else {
				maxLeft = left;
			}

			left++;
		} else {
			// max left higher
			if (height[right] < height[maxRight]) {
				total += height[maxRight] - height[right];
			} else {
				maxRight = right;
			}

			right--;
		}
	}

	return total;
}
