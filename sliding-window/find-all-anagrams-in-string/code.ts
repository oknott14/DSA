function setIsEqual(s1: Map<string, number>, s2: Map<string, number>) {
	if (s1.size != s2.size) {
		return false;
	}

	for (const key of s1.keys()) {
		if (s1.get(key) != s2.get(key)) return false;
	}

	return true;
}

export function findAnagrams(s: string, p: string): number[] {
	if (p.length > s.length) {
		return [];
	}

	const starts: number[] = [];

	const anagramCount: Map<string, number> = new Map();
	const currentCount: Map<string, number> = new Map();
	let idx: number;

	for (idx = 0; idx < p.length && idx < s.length; idx++) {
		anagramCount.set(p[idx], (anagramCount.get(p[idx]) ?? 0) + 1);
		currentCount.set(s[idx], (currentCount.get(s[idx]) ?? 0) + 1);
	}

	for (idx = p.length; idx < s.length; idx++) {
		// If the current set is equal add start index to soln
		if (setIsEqual(currentCount, anagramCount)) {
			starts.push(idx - p.length);
		}

		// Add if new char is in set
		if (currentCount.has(s[idx])) {
			currentCount.set(s[idx], currentCount.get(s[idx])! + 1);
		} else {
			// initialize it as 1 if not
			currentCount.set(s[idx], 1);
		}

		// Remove tail if only 1 exist
		if (currentCount.get(s[idx - p.length])! == 1) {
			currentCount.delete(s[idx - p.length]);
		} else {
			// Otherwise decrement count
			currentCount.set(
				s[idx - p.length],
				currentCount.get(s[idx - p.length])! - 1,
			);
		}
	}

	if (setIsEqual(currentCount, anagramCount)) {
		starts.push(s.length - p.length);
	}

	return starts;
}
