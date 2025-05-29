const primes = [
	2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
	73, 79, 83, 89, 97, 103,
];
export function groupAnagrams(strs: string[]): string[][] {
	let groups: Record<number, string[]> = {};
	let prod: number;
	for (let word of strs) {
		prod = 1;

		for (let idx = 0; idx < word.length; idx++) {
			prod *= primes[word.charCodeAt(idx) - 97];
		}

		if (groups[prod]) {
			groups[prod].push(word);
		} else {
			groups[prod] = [word];
		}
	}
	return Object.values(groups);
}
