export function characterReplacement(s: string, k: number): number {
	let left: number = 0;
	let max: number = 0;
	let freq: Array<number> = new Array(26).fill(0);

	for (let right = 0; right < s.length; right++) {
		max = Math.max(max, ++freq[s.charCodeAt(right) - 65]);

		if (right - left + 1 - max > k) {
			freq[s.charCodeAt(left) - 65]--;
			left++;
		}
	}

	return s.length - left;
}
