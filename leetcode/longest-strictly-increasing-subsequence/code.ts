export function lengthOfLIS(nums: number[]): number {
	if (!nums.length) return 0;
	let sub: number[] = [nums[0]];
	let left: number;
	let right: number;
	let mid: number;
	for (let num of nums.slice(1)) {
		if (sub[sub.length - 1] < num) {
			sub.push(num);
		} else {
			left = 0;
			right = sub.length - 1;
			do {
				mid = Math.floor((left + right) / 2);

				if (num <= sub[mid]) {
					right = mid;
				} else {
					left = mid + 1;
				}
			} while (right != left);

			sub[right] = num;
		}
	}
	return sub.length;
}
