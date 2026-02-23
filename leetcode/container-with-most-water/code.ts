export function maxArea(height: number[]): number {
	let left = 0;
	let right = height.length - 1;

	let maxArea = 0;

	while (right > left) {
		maxArea = Math.max(
			maxArea,
			Math.min(height[right], height[left]) * (right - left),
		);

		if (height[right] > height[left]) {
			left++;
		} else {
			right--;
		}
	}

	return maxArea;
}
