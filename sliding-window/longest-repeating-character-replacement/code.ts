export function characterReplacement(s: string, k: number): number {
	if (s.length == 0) return 0;

	let left = 0;
	let right = 0;
	let max = 0;
	let freq = new Map<string, number>();

	while (right < s.length) {
		if (freq.has(s[right])) {
			freq.set(s[right], freq.get(s[right])! + 1);
		} else {
			freq.set(s[right], 1);
		}

		max = Math.max(max, freq.get(s[right])!);

		right++;

		if (right - left - max > k) {
			freq.set(s[left], freq.get(s[left])! - 1);
			left++;
		}
	}

	return s.length - left;
}

export function characterReplacementOld(s: string, k: number): number {
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
