export function lengthOfLongestSubstring(s: string): number {
	let left = 0;
	let right = 0;
	let longest = 0;
	const charsInWindow = new Set<string>();

	while (right < s.length) {
		if (charsInWindow.has(s[right])) {
			left++;
			while (s[left - 1] != s[right]) {
				charsInWindow.delete(s[left - 1]);
				left++;
			}
		} else {
			charsInWindow.add(s[right]);
		}

		right++;
		longest = Math.max(longest, right - left);
	}

	return longest;
}
