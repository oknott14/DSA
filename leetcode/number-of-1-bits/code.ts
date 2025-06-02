export function hammingWeight(n: number): number {
	let numOnes = 0;
	while (n) {
		numOnes += n & 1;
		n >>= 1;
	}

	return numOnes;
}
